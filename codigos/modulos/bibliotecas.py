import os # Biblioteca os = Sistema operacional, permite você acessar as coisas do seu computador

# .listdir é uma função que  lista tudo que está no seu diretório
arquivos = os.listdir()
print(arquivos) # ['.git', '.gitattributes', 'codigos', 'exercicios', 'LICENSE', 'README.md']

os.rename("ex011.py", "exercicios/ex011.py") # Renomear o arquivo, e também muda-lo de lugar