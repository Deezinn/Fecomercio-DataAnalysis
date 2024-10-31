from etlbc import *
class Main: 
    def __init__(self):
        pass
    
    def iniciar_etl(self):
        # Link de Expectativa de Mercado Mensal
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativaMercadoMensais', 'ExpectativaMercadoMensais.csv')
        
        # Link de Expectativa de Mercado Selic
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoSelic?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoSelic', 'ExpectativasMercadoSelic.csv')
        
        # Link de Expectativa de Mercado Trimestral
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoTrimestrais', 'ExpectativasMercadoTrimestrais.csv')
        
        # Link de Expectativa de Mercado Anual
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoAnuais', 'ExpectativasMercadoAnuais.csv')
        
        # Link de Quantidade de Transações de Cartões Trimestral
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'QuantidadeTransacoesCartoesTrimestral', 'QuantidadeTransacoesCartoesTrimestral.csv')
        
        # Link de Meios de Pagamento Mensal
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosMensalDA(AnoMes=@AnoMes)?@AnoMes='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosMensal', 'MeiosPagamentosMensal.csv')
        
        # Link de Meios de Pagamento Trimestral
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosTrimestral', 'MeiosPagamentosTrimestral.csv')

etl_main = Main()
etl_main.iniciar_etl()