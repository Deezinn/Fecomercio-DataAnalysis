from etlbc import *
from pmsVendasEstados import *
from pmsVendas import *
from pmsCargaBrasil import *

class Main: 
    def __init__(self):
        pass
    
    def iniciar_etl(self):
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativaMercadoMensais')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoSelic?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoSelic')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoTrimestrais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoTrimestrais')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'ExpectativasMercadoAnuais')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'QuantidadeTransacoesCartoesTrimestral')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosMensalDA(AnoMes=@AnoMes)?@AnoMes='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosMensal')
        
        url = "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20201'&$top=100000&$format=json"
        etl = ETLBcb(url)
        etl.executar_etl('value', 'MeiosPagamentosTrimestral')
        
        url = "https://servicodados.ibge.gov.br/api/v3/agregados/8693/periodos/201102-202407/variaveis/11623?localidades=N3[all]&classificacao=11046[56726]|12355[all]"
        etl = PMSVendasEstados(url)
        etl.executar_etl('resultados', 'pmsVendasEstado')
        
        url = 'https://servicodados.ibge.gov.br/api/v3/agregados/8688/periodos/201102-202407/variaveis/11623?localidades=N1[all]&classificacao=11046[56726]|12355[107071,106869,106874,31399,106876,31426]'
        etl = PmsVendas(url)
        etl.executar_etl('resultados', 'pmsVendas')
        
        url = 'https://servicodados.ibge.gov.br/api/v3/agregados/8695/periodos/201102-202407/variaveis/11623?localidades=N1[all]&classificacao=11046[56726]|12355[56724]'
        etl = PMSCargaBrasil(url)
        etl.executar_etl('pmsCargaBrasil')

etl_main = Main()
etl_main.iniciar_etl()
