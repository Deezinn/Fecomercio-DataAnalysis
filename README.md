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

## 🛠️ Como Utilizar
1. Clone o repositório para a sua máquina.
2. Certifique-se de ter o Python e o Conda instalados.
3. Configure o ambiente com todas as dependências.
4. Execute a ETL para iniciar o processo de extração, transformação e carregamento de dados.
