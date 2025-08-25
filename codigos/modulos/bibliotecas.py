""" import os # Biblioteca os = Sistema operacional, permite você acessar as coisas do seu computador, essa biblioteca já vem instalada no python

# .listdir é uma função que  lista tudo que está no seu diretório
arquivos = os.listdir()
print(arquivos) # ['.git', '.gitattributes', 'codigos', 'exercicios', 'LICENSE', 'README.md']

# os.rename("codigos/modulos/ex011.py", "exercicios/ex011.py") # Renomear o arquivo, e também muda-lo de lugar """



# Para instalar bibliotecas no terminal, use o comando: pip install nome_da_biblioteca
# Exemplo: pip install requests

import requests  # Importa a biblioteca 'requests', usada para fazer requisições HTTP

# URL da AwesomeAPI que retorna as cotações em tempo real do Dólar, Euro e Bitcoin em relação ao Real
link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

# Faz a requisição GET para a API e armazena a resposta
resposta = requests.get(link)

# Converte a resposta em formato JSON para um dicionário Python
dicionario_resp = resposta.json()

# Exemplo da estrutura retornada pela API:
"""
{
  'USDBRL': {
    'code': 'USD',
    'codein': 'BRL',
    'name': 'Dólar Americano/Real Brasileiro',
    'high': '5.4472',
    'low': '5.40897',
    'varBid': '0.0062',
    'pctChange': '0.11435',
    'bid': '5.4282',
    'ask': '5.4312',
    'timestamp': '1756127518',
    'create_date': '2025-08-25 10:11:58'
  },
  ...
}
"""

# Acessa o dicionário correspondente à cotação do Dólar
cotacao_dolar = dicionario_resp["USDBRL"]

# Imprime o valor atual de compra (bid) do Dólar em Reais
print(cotacao_dolar["bid"])  # Exemplo de saída: 5.4282


