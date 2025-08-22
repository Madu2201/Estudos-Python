# 📁 Manipulação de Arquivos em Python

A manipulação de arquivos é uma habilidade essencial para qualquer programador Python. Ela permite ler, escrever e processar dados armazenados em arquivos de texto, binários ou estruturados como CSV e JSON.

---

## 🔓 Abrindo Arquivos

Python oferece duas formas principais de abrir arquivos:

### ✅ Modo tradicional
```python
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()
```

**É necessário fechar o arquivo manualmente com close().**


### ✅ Modo automático com with
```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
```

**O with garante que o arquivo será fechado automaticamente ao final do bloco.**

## ✍️ Modos de Abertura de Arquivos em Python

| Modo | Descrição                                 |
|------|-------------------------------------------|
| `"r"`  | Leitura (erro se o arquivo não existir)   |
| `"w"`  | Escrita (cria ou sobrescreve o arquivo)   |
| `"a"`  | Escrita (adiciona conteúdo ao final)      |
| `"x"`  | Criação (erro se o arquivo já existir)    |
| `"rb"` | Leitura em modo binário                  |
| `"wb"` | Escrita em modo binário                  |


---


## 📖 Lendo Arquivos


### `.read()`
Lê todo o conteúdo como uma única string.
```python
texto = arquivo.read()
```


### `.readlines()`
Retorna uma lista onde cada item é uma linha do arquivo.
```python
linhas = arquivo.readlines()
```


### `.readline()`
Lê uma linha por vez.
```python
linha = arquivo.readline()
```

---

## 🧹 Tratando Linhas
Ao ler arquivos, é comum limpar e separar os dados:
```python
linha = linha.strip()           # Remove espaços e quebras de linha
dados = linha.split(",")        # Separa por vírgula
```

---

## 📝 Escrevendo em Arquivos
Criar ou sobrescrever:
```python
with open("saida.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
```

---

## Adicionar ao final:
```python
with open("saida.txt", "a") as arquivo:
    arquivo.write("Nova linha\n")
```

---

## 📂 Caminhos de Arquivo

### Caminho relativo:
```python
open("dados.txt", "r")
```


### Caminho absoluto:
```python
open("C:/Users/usuario/Documents/dados.txt", "r")
```


### Compatibilidade entre sistemas:
```python
import os
caminho = os.path.join("pasta", "dados.txt")
open(caminho, "r")
```

---

## ✅ Boas Práticas
**1° Use with open(...) para garantir fechamento automático.**

**2° Verifique se o arquivo existe com os.path.exists().**

**3° Evite caminhos com espaços ou acentuação.**

**4° Trate exceções com try/except para evitar falhas inesperadas.**




