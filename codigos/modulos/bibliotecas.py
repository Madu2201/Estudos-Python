""" import os # Biblioteca os = Sistema operacional, permite você acessar as coisas do seu computador, essa biblioteca já vem instalada no python

# .listdir é uma função que  lista tudo que está no seu diretório
arquivos = os.listdir()
print(arquivos) # ['.git', '.gitattributes', 'codigos', 'exercicios', 'LICENSE', 'README.md']

# os.rename("codigos/modulos/ex011.py", "exercicios/ex011.py") # Renomear o arquivo, e também muda-lo de lugar """


# No command prompt coloque: pip install nome da biblioteca =pip é o que faz instalação de bibliotecas
import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL" # Link do Awesome API que faz a requisição do dólar em real, euro e bitcoin em tempo real

resposta = requests.get(link)
dicionario_resp = resposta.json()
# print(dicionario_resp)

""" dicionario_resp
{'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '5.4472', 'low': '5.40897', 'varBid': '0.0062', 'pctChange': '0.11435', 'bid': '5.4282', 'ask': '5.4312', 'timestamp': '1756127518', 'create_date': '2025-08-25 10:11:58'}, 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '6.37349', 'low': '6.32911', 'varBid': '0.004028', 'pctChange': '0.063525', 'bid': '6.34518', 'ask': '6.36132', 'timestamp': '1756127512', 'create_date': '2025-08-25 10:11:52'}, 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '626240', 'low': '603789', 'varBid': '-17985', 'pctChange': '-2.879', 'bid': '606669', 'ask': '606670', 'timestamp': '1756127526', 'create_date': '2025-08-25 10:12:06'}} 
"""

cotacao_dolar = dicionario_resp["USDBRL"]
print(cotacao_dolar["bid"]) # 'bid': '5.4282' que é o valor da cotação do dólar

