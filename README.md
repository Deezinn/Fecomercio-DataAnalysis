# 📊 Sistema de Análise de Dados

## 📝 Descrição
Este projeto foi desenvolvido para a Fecomércio com o objetivo de criar um sistema robusto de análise de dados. Através do uso de ferramentas poderosas como Python, Pandas e Power BI, ele permite o processamento e a análise eficaz de grandes volumes de dados, fornecendo insights valiosos para a tomada de decisões estratégicas da organização. A ETL do sistema realiza a extração de dados de diferentes APIs e arquivos CSV/JSON, transforma essas informações e as armazena em um banco de dados SQLite para uso posterior nas análises.

## 🚀 Funcionalidades
- **📂 Extração de Dados**: Coleta informações de múltiplas fontes, como APIs do IBGE e Banco Central.
- **🛠️ Transformação de Dados**: Realiza a manipulação e limpeza dos dados usando Pandas, garantindo que os dados estejam prontos para análise.
- **💾 Armazenamento de Dados**: Os dados transformados são salvos em um banco de dados SQLite para consultas futuras.
- **📊 Visualização de Dados**: Integração com o Power BI para criar relatórios interativos e dashboards personalizados, facilitando a visualização de tendências e métricas importantes.

## 🛠️ Tecnologias Utilizadas
- **🐍 Python**: Linguagem de programação principal, utilizada para automação e manipulação de dados.
- **📊 Pandas**: Biblioteca de análise de dados que facilita o tratamento de grandes volumes de informação.
- **💻 Power BI**: Ferramenta de visualização que transforma os dados em gráficos e dashboards interativos.
- **🗄️ SQLite**: Banco de dados leve utilizado para armazenar os dados processados.
- **🌐 APIs**: Dados extraídos de APIs públicas, como IBGE e Banco Central, em formatos JSON e CSV.

## 📂 Estrutura do Projeto
- `/datasets/csv`: Pasta destinada ao armazenamento dos arquivos CSV extraídos e transformados.
- `fecomdb.db`: Banco de dados SQLite onde os dados processados são armazenados.
- `readme.md`: Documentação do projeto com detalhes sobre as funcionalidades e tecnologias.

## 📘 Documentação  

A documentação adicional do projeto detalha:  

- **Descrição Geral**:  
  Este projeto foi desenvolvido com o objetivo de consolidar e analisar uma ampla gama de dados econômicos e financeiros, abrangendo indicadores macroeconômicos (como IPCA e Taxa Selic) e transações financeiras realizadas por diferentes meios de pagamento, como PIX, boletos, TEDs e cartões de crédito/débito.  

- **Estrutura dos Painéis**:  
  Os dashboards foram projetados para destacar as relações entre as variáveis econômicas e o comportamento dos consumidores em diferentes períodos. Eles oferecem uma interface moderna e interativa, permitindo:  
  - **Análises históricas**.  
  - **Projeções futuras**.  
  - Personalização por meio de **filtros dinâmicos**.  

- **Navegação no Dashboard**:  
  Na página inicial, os usuários podem acessar diferentes abas, cada uma dedicada a um tema específico:  
  - **Cartões**: Dados sobre volume de transações e tendências de uso.  
  - **Meios de Pagamento**: Comparativo entre métodos como PIX, boletos e TEDs.  
  - **Pesquisa Mensal de Serviço**: Análises setoriais detalhadas.  
  - **Expectativa de Mercado**: Indicadores de confiança econômica e projeções de mercado.  

  Cada aba é dividida em seções para facilitar a navegação e a compreensão dos dados apresentados.  
  

## 🛠️ Como Utilizar
1. Clone o repositório para a sua máquina.
2. Certifique-se de ter o Python e o Conda instalados.
3. Configure o ambiente com todas as dependências.
4. Execute a ETL para iniciar o processo de extração, transformação e carregamento de dados.
