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

class PMSCargaBrasil:
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
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição à API: {e}")

    def transformar_dados(self):
        """
        Método para transformar os dados JSON em um DataFrame pandas.
        Aqui fazemos o acesso seguro aos dados e transformamos a série temporal em DataFrame.
        """
        if self.dados:
            try:
                # Acessar as classificações de forma segura
                classificacao = []
                try:
                    # Aqui estamos acessando o segundo item de 'classificacoes' de forma segura
                    classificacao = list(self.dados[0]['resultados'][0].get('classificacoes', [])[1].get('categoria', {}).values())
                except (IndexError, KeyError) as e:
                    print(f"Erro ao acessar classificações: {e}")

                # Extrair a série temporal de Transporte de Cargas de forma segura
                serie_temporal = []
                try:
                    serie_temporal = self.dados[0]['resultados'][0].get('series', [])[0].get('serie', {})
                except (IndexError, KeyError) as e:
                    print(f"Erro ao acessar série temporal: {e}")

                # Converter a série temporal em um DataFrame
                if serie_temporal:
                    df_cargas = pd.DataFrame(list(serie_temporal.items()), columns=['Data', 'Transporte de Cargas'])
                    df_cargas['Data'] = pd.to_datetime(df_cargas['Data'], format='%Y%m')
                    self.df = df_cargas  # Armazena o DataFrame no atributo df
                else:
                    print("Série temporal não encontrada ou vazia.")

            except Exception as e:
                print('Erro ao transformar os dados:', e)
        else:
            print('Nenhum dado para transformar.')

    def salvar_sqlite(self, nome_tabela):
        """
        Método para salvar o DataFrame transformado em um banco de dados SQLite.
        """
        nome_banco = os.path.join(db_directory, 'Fecomdb.db')
        if self.df is not None and not self.df.empty:
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

    def executar_etl(self, nome_tabela):
        """
        Método para executar todo o processo de ETL.
        """
        # Executar extração
        self.requisicao_api()

        # Transformar os dados
        self.transformar_dados()

        # Salvar no banco SQLite
        self.salvar_sqlite(nome_tabela)
