import os # Biblioteca os = Sistema operacional, permite você acessar as coisas do seu computador, essa biblioteca já vem instalada no python

# .listdir é uma função que  lista tudo que está no seu diretório
arquivos = os.listdir()
print(arquivos) # ['.git', '.gitattributes', 'codigos', 'exercicios', 'LICENSE', 'README.md']

# os.rename("codigos/modulos/ex011.py", "exercicios/ex011.py") # Renomear o arquivo, e também muda-lo de lugar


# No command prompt coloque: pip install nome da biblioteca =pip é o que faz instalação de bibliotecas
import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL" # Link que faz a requisição do dólarm real, euro e bitcoin em tempo real

resposta = requests.get()


