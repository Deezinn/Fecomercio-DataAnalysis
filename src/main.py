from etlbc import *
from pmsVendas import *

class Main: 
    def __init__(self):
        pass
    
    def iniciar_etl(self):
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativaMercadoMensais', 'ExpectativaMercadoMensais.csv')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoSelic?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoSelic', 'ExpectativasMercadoSelic.csv')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoTrimestrais', 'ExpectativasMercadoTrimestrais.csv')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoAnuais', 'ExpectativasMercadoAnuais.csv')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'QuantidadeTransacoesCartoesTrimestral', 'QuantidadeTransacoesCartoesTrimestral.csv')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosMensalDA(AnoMes=@AnoMes)?@AnoMes='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosMensal', 'MeiosPagamentosMensal.csv')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosTrimestral', 'MeiosPagamentosTrimestral.csv')
        
        url = "https://servicodados.ibge.gov.br/api/v3/agregados/8693/periodos/201102-202407/variaveis/11623?localidades=N3[all]&classificacao=11046[56726]|12355[all]"
        etl = PMSVendas(url)
        etl.executar_etl('resultados', 'pmsVendas', 'pmsVendas.csv')

etl_main = Main()
etl_main.iniciar_etl()
