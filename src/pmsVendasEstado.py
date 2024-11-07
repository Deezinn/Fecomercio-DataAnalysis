import requests
import json
import pandas as pd
import sqlite3
import os

# Diretório principal onde os arquivos serão salvos
base_directory = "datasets"
db_directory = os.path.join(base_directory, "db")

# Verifica e cria os diretórios se não existirem
if not os.path.exists(base_directory):
    os.makedirs(base_directory)
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

class PMSVendasEstado:
    def __init__(self, api_link):
        self.api_link = api_link
        self.dados = None
        self.df = None

    def requisicao_api(self):
        """
        Método para fazer a requisição à API e armazenar os dados.
        """
        try:
            response = requests.get(self.api_link)
            response.raise_for_status()  # Vai gerar uma exceção para códigos de erro HTTP
            self.dados = response.json()  # Converte a resposta em JSON
            print(f"Dados recebidos da API: {len(self.dados)} itens.")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição à API: {e}")

    def transformar_dados(self, chave_json='resultados'):
        """
        Método para transformar os dados JSON em um DataFrame pandas.
        """
        if self.dados:
            try:
                # Acessa o primeiro item de `self.dados` se for uma lista
                data = self.dados[0] if isinstance(self.dados, list) else self.dados
                
                # Obtém o conteúdo da chave "resultados"
                resultados = data.get(chave_json, [])
                
                # Verifica se `resultados` não está vazio
                if resultados:
                    # Extrair todas as séries e localizações
                    series_data = []
                    for resultado in resultados:
                        if 'series' in resultado:
                            for serie_info in resultado['series']:
                                # Extraindo as informações de localidade e série
                                for serie in serie_info['serie']:
                                    localidade_nome = serie_info['localidade']['nome']
                                    serie_valor = serie
                                    series_data.append({
                                        'localidade_nome': localidade_nome,
                                        'serie': serie_valor
                                    })

                    # Cria um DataFrame com todos os dados das séries
                    self.df = pd.DataFrame(series_data)

                    # Salva o DataFrame transformado
                    print('Transformação concluída.')
                else:
                    print(f'Nenhum dado encontrado na chave "{chave_json}".')
            except KeyError as e:
                print(f'Chave não encontrada: {e}')
            except Exception as e:
                print('Erro ao transformar os dados:', e)
        else:
            print('Nenhum dado para transformar.')

    def salvar_sqlite(self, nome_tabela):
        """
        Método para salvar o DataFrame transformado em um banco de dados SQLite.
        """
        nome_banco = os.path.join(db_directory, 'Fecomdb.db')
        if self.df is not None:
            try:
                # Converte listas para strings para compatibilidade com SQLite
                for coluna in self.df.columns:
                    if isinstance(self.df[coluna].iloc[0], list):
                        self.df[coluna] = self.df[coluna].apply(lambda x: json.dumps(x) if isinstance(x, list) else x)
            
                with sqlite3.connect(nome_banco) as conexao:
                    self.df.to_sql(nome_tabela, conexao, if_exists='replace', index=False)
                print(f'Dados salvos na tabela "{nome_tabela}" do banco de dados "{nome_banco}".')
            except Exception as e:
                print('Erro ao salvar os dados no banco de dados SQLite:', e)
        else:
            print('Nenhum dado para salvar no banco de dados.')

    def salvar_csv(self, nome_arquivo):
        """
        Método para salvar o CSV.
        """
        if self.df is not None:
            try:
                caminho_csv = os.path.join(base_directory, nome_arquivo)
                self.df.to_csv(caminho_csv, sep=';', decimal=',', encoding='utf-8-sig')
                print(f'Dados salvos no arquivo CSV "{caminho_csv}".')
            except Exception as e:
                print('Erro ao salvar o CSV:', e)
        else:
            print('Nenhum dado no CSV.')

    def executar_etl(self, chave_json, nome_tabela, nome_arquivo):
        """
        Método para executar todo o processo de ETL.
        """
        # Executar extração
        self.requisicao_api()

        # Transformar os dados
        self.transformar_dados(chave_json)

        # Salvar no banco SQLite
        self.salvar_sqlite(nome_tabela)

        # Salvar em CSV
        self.salvar_csv(nome_arquivo)
