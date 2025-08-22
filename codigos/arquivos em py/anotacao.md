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

É necessário fechar o arquivo manualmente com close().
```

### Modo automático com with
```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

O with garante que o arquivo será fechado automaticamente ao final do bloco.
```
