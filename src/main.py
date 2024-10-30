from etl import *
class Main: 
    def __init__(self):
        pass
    
    def iniciar_etl(self):
        # Link de Expectativa de Mercado Mensal
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'ExpectativaMercadoMensais', 'ExpectativaMercadoMensais.csv')
        
        # Link de Expectativa de Mercado Selic
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoSelic?$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoSelic', 'ExpectativasMercadoSelic.csv')
        
        # Link de Expectativa de Mercado Trimestral
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoTrimestrais', 'ExpectativasMercadoTrimestrais.csv')
        
        # Link de Expectativa de Mercado Anual
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoAnuais', 'ExpectativasMercadoAnuais.csv')
        
        # Link de Quantidade de Transações de Cartões Trimestral
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'QuantidadeTransacoesCartoesTrimestral', 'QuantidadeTransacoesCartoesTrimestral.csv')
        
        # Link de Meios de Pagamento Mensal
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosMensalDA(AnoMes=@AnoMes)?@AnoMes='20201'&$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosMensal', 'MeiosPagamentosMensal.csv')
        
        # Link de Meios de Pagamento Trimestral
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = etlBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosTrimestral', 'MeiosPagamentosTrimestral.csv')

        # PMS - VENDAS
        url = 'https://servicodados.ibge.gov.br/api/v3/agregados/8688/periodos/201101-202407/variaveis/11623?localidades=N1[all]&classificacao=11046[56726]|12355[all]'
        etl = etlBcb(url)
        etl.executar_etl('resultados', 'PMS_VENDAS', 'PMS_VENDAS.csv') 

        # PMS - VENDAS ESTADOS
        url = 'https://servicodados.ibge.gov.br/api/v3/agregados/8693/periodos/201101-202407/variaveis/11623?localidades=N3[all]&classificacao=11046[56726]|12355[all]'
        etl = etlBcb(url)
        etl.executar_etl('resultados', 'PMS_VENDAS_ESTADOS', 'PMS_VENDAS_ESTADOS.csv') 

        # PMS - CARGAS
        url = 'https://servicodados.ibge.gov.br/api/v3/agregados/8695/periodos/201101-202407/variaveis/11623?localidades=N1[all]&classificacao=11046[56726]|12355[56724]'
        etl = etlBcb(url)
        etl.executar_etl('resultados', 'PMS_CARGAS', 'PMS_CARGAS.csv') 


etl_main = Main()
etl_main.iniciar_etl()