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

class ETLBcb:
    def __init__(self, api_link):
        self.api_link = api_link
        self.dados = None
        self.df = None

    def requisicao_api(self):
        """
        Método GET para a API e armazena a resposta.
        """
        try:
            resposta = requests.get(self.api_link)
            if resposta.status_code == 200:
                self.dados = resposta.json()
                print('Status Code:', resposta.status_code)
            else:
                print('Erro na requisição. Status Code:', resposta.status_code)
        except Exception as e:
            print('Erro ao fazer a requisição:', e)

    def transformar_dados(self, chave_json):
        """
        Método para transformar os dados JSON em um DataFrame pandas.
        """
        if self.dados:
            try:
                data = self.dados.get(chave_json, [])
                self.df = pd.json_normalize(data)

                # Verificar e converter colunas de data
                if 'trimestre' in self.df.columns:
                    print('Coluna "trimestre" encontrada, convertendo para datas...')
                    self.df['trimestre'] = self.df['trimestre'].astype(str)
                    self.df['data'] = self.df['trimestre'].apply(self.trimestre_para_data)
                    self.df['data'] = self.df['data'].dt.date
                elif 'AnoMes' in self.df.columns:
                    print('Coluna "AnoMes" encontrada, convertendo para datas...')
                    self.df['AnoMes'] = self.df['AnoMes'].astype(str)
                    self.df['data'] = self.df['AnoMes'].apply(self.anoMes_para_data)
                    self.df['data'] = self.df['data'].dt.date
                elif 'Data' in self.df.columns:
                    print('Coluna "Data" encontrada, convertendo para datas...')
                    self.df['Data'] = pd.to_datetime(self.df['Data']).dt.date
                else:
                    print('Nenhuma coluna de data encontrada nos dados.')
                
                print('Transformação concluída.')
            except KeyError:
                print(f'Chave "{chave_json}" não encontrada nos dados JSON.')
            except Exception as e:
                print('Erro ao transformar os dados:', e)
        else:
            print('Nenhum dado para transformar.')

    @staticmethod
    def trimestre_para_data(trimestre):
        """
        Função para converter o formato de trimestre para data.
        """
        try:
            ano = int(trimestre[:4])
            trimestre_num = int(trimestre[-1])
            mes = (trimestre_num - 1) * 3 + 1
            return pd.to_datetime(f"{ano}-{mes:02d}-01")
        except ValueError:
            print(f"Erro ao converter o trimestre: {trimestre}")
            return pd.NaT

    @staticmethod
    def anoMes_para_data(AnoMes):
        """
        Função para converter o formato de AnoMes (ex: 202202) para data.
        """
        try:
            ano = int(AnoMes[:4])
            mes = int(AnoMes[4:6])
            return pd.to_datetime(f"{ano}-{mes:02d}-01")
        except ValueError:
            print(f"Erro ao converter o mês/ano: {AnoMes}")
            return pd.NaT

    def salvar_sqlite(self, nome_tabela):
        """
        Método para salvar o DataFrame transformado em um banco de dados SQLite.
        """
        nome_banco = os.path.join(db_directory, 'Fecomdb.db')
        if self.df is not None:
            try:
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
