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

class PmsVendas:
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
        Método para transformar os dados JSON em um DataFrame pandas e organizar as séries.
        """
        if self.dados:
            try:
                # Acessa o primeiro item de `self.dados` se for uma lista
                data = self.dados[0] if isinstance(self.dados, list) else self.dados
                
                # Obtém o conteúdo da chave "resultados"
                resultados = data.get(chave_json, [])
                
                # Verifica se `resultados` não está vazio
                if resultados:
                    series_dict = {}
                    for i in range(len(resultados)):
                        # Extrair o nome da coluna
                        nome_coluna = list(resultados[i]['classificacoes'][1]['categoria'].values())[0]

                        # Extrair os valores da série
                        serie_valores = resultados[i]['series'][0]['serie']

                        # Adicionar a série ao dicionário
                        series_dict[nome_coluna] = serie_valores

                    # Criar um DataFrame a partir do dicionário de séries
                    df_series = pd.DataFrame(series_dict)

                    # Adicionar a coluna de Data como índice (anos-meses)
                    df_series.index = resultados[0]['series'][0]['serie'].keys()

                    # Certificar que o índice está no formato datetime para posterior análise
                    df_series.index = pd.to_datetime(df_series.index, format='%Y%m')

                    # Renomear o índice para "Data"
                    df_series.index.name = "Data"

                    # Atribuir ao atributo da classe
                    self.df = df_series

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
                with sqlite3.connect(nome_banco) as conexao:
                    self.df.to_sql(nome_tabela, conexao, if_exists='replace', index=True)
                print(f'Dados salvos na tabela "{nome_tabela}" do banco de dados "{nome_banco}".')
            except Exception as e:
                print('Erro ao salvar os dados no banco de dados SQLite:', e)
        else:
            print('Nenhum dado para salvar no banco de dados.')

    def executar_etl(self, chave_json, nome_tabela):
        """
        Método para executar todo o processo de ETL.
        """
        # Executar extração
        self.requisicao_api()

        # Transformar os dados
        self.transformar_dados(chave_json)

        # Salvar no banco SQLite
        self.salvar_sqlite(nome_tabela)
