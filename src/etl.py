import requests
import json
import pandas as pd
import sqlite3
import os
import shutil  # Para mover arquivos

# Diretório onde os arquivos serão salvos
directory = "datasets"
db_directory = os.path.join(directory, "db")  # Diretório para o banco de dados

# Verifica se o diretório já existe, caso contrário, cria o diretório
if not os.path.exists(directory):
    os.makedirs(directory)

# Cria a pasta "db" dentro do diretório "datasets"
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

class etlBcb:
    def __init__(self, api_link):
        self.api_link = api_link
        self.dados = None
        self.df = None

    def requisicao_api(self):
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
        if self.dados:
            try:
                data = self.dados[chave_json]
                self.df = pd.json_normalize(data)

                if 'trimestre' in self.df.columns:
                    print('Coluna "trimestre" encontrada, convertendo para datas...')
                    self.df['trimestre'] = self.df['trimestre'].astype(str)
                    self.df['data'] = self.df['trimestre'].apply(self.trimestre_para_data)
                    self.df['data'] = self.df['data'].dt.date  
                if 'AnoMes' in self.df.columns:
                    print('Coluna "AnoMes" encontrada, convertendo para datas...')
                    self.df['AnoMes'] = self.df['AnoMes'].astype(str)
                    self.df['data'] = self.df['AnoMes'].apply(self.anoMes_para_data)
                    self.df['data'] = self.df['data'].dt.date  
                if 'Data' in self.df.columns:
                    print('Coluna "Data" encontrada, convertendo para datas...')
                    self.df['Data'] = self.df['Data'].astype(str)
                    self.df['Data'] = pd.to_datetime(self.df['Data']).dt.date
                else:
                    print('Coluna "trimestre" não encontrada nos dados.')
                print('Transformação concluída.')
            except KeyError:
                print(f'Chave "{chave_json}" não encontrada nos dados JSON.')
            except Exception as e:
                print('Erro ao transformar os dados:', e)
        else:
            print('Nenhum dado para transformar.')

    @staticmethod
    def trimestre_para_data(trimestre):
        try:
            ano = int(str(trimestre)[:4])
            trimestre_num = int(str(trimestre)[-1])
            mes = (trimestre_num - 1) * 3 + 1
            return pd.to_datetime(f"{ano}-{mes:02d}-01")
        except ValueError:
            print(f"Erro ao converter o trimestre: {trimestre}")
            return pd.NaT

    @staticmethod
    def anoMes_para_data(AnoMes):
        try:
            ano = int(str(AnoMes)[:4])  
            mes = int(str(AnoMes)[4:6])  
            return pd.to_datetime(f"{ano}-{mes:02d}-01")  
        except ValueError:
            print(f"Erro ao converter o mês/ano: {AnoMes}")
            return pd.NaT

    def salvar_sqlite(self, nome_tabela):
        nome_banco = 'Fecomdb.db'
        if self.df is not None:
            try:
                conexao = sqlite3.connect(nome_banco)
                self.df.to_sql(nome_tabela, conexao, if_exists='replace', index=False)
                conexao.close()
                print(f'Dados salvos na tabela "{nome_tabela}" do banco de dados "{nome_banco}".')
                
                # Move o banco de dados para a pasta "db"
                destination_path = os.path.join(db_directory, nome_banco)
                
                # Verifica se o arquivo já existe e lida com isso
                if os.path.exists(destination_path):
                    # Se existir, remove o arquivo antigo
                    os.remove(destination_path)
                    print(f'Arquivo existente removido: {destination_path}')
                
                shutil.move(nome_banco, destination_path)
                print(f'Banco de dados movido para a pasta "{db_directory}".')
                
            except Exception as e:
                print('Erro ao salvar os dados no banco de dados SQLite:', e)
        else:
            print('Nenhum dado para salvar no banco de dados.')

    def salvar_csv(self, nome_arquivo):
        if self.df is not None:
            try:
                self.df.to_csv(f'{directory}/{nome_arquivo}', sep=';', decimal=',', encoding='utf-8-sig')
                print(f'Dados salvos no arquivo CSV "{nome_arquivo}".')
            except Exception as e:
                print('Erro ao salvar o CSV:', e)
        else:
            print('Nenhum dado no CSV.')

    def executar_etl(self, chave_json, nome_tabela, nome_arquivo):
        self.requisicao_api()
        self.transformar_dados(chave_json)
        self.salvar_sqlite(nome_tabela)
        self.salvar_csv(nome_arquivo)
