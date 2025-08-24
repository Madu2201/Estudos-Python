# 📦 Explicação do Código Python — Organização de Arquivos .txt

[Ver código completo](automacao.py)

---

```python
import os  # Importa a biblioteca que interage com o sistema operacional
```

**O módulo os permite que o Python acesse funcionalidades do sistema operacional, como manipular arquivos, pastas e caminhos.**


```python
lista_arquivos = os.listdir("codigos/arquivos")
Cria uma lista com todos os nomes de arquivos e pastas dentro do diretório codigos/arquivos.
```

**Retorna uma lista como: ['arquivo22.txt', 'arquivo23.txt', '22', '23'].**


```python
for nome in lista_arquivos:
Inicia um laço que percorre cada item da lista lista_arquivos.
```

**A variável nome representa o nome de cada arquivo ou pasta encontrado.**


```python
if nome.endswith(".txt"):
Verifica se o item atual é um arquivo .txt.
```

**Garante que o código só vai tentar mover arquivos de texto, ignorando pastas ou outros tipos de arquivos.**


```python
try:
```

**Inicia um bloco de tentativa.**

**Tudo dentro do try será executado, e se ocorrer algum erro, será tratado pelo except.**


```python
if "22" in nome:
    os.rename(f"codigos/arquivos/{nome}", f"codigos/arquivos/22/{nome}")
    print(f"✅ '{nome}' movido para pasta 22 com sucesso.")
Verifica se o nome do arquivo contém "22".
```

**Se sim, move o arquivo para a subpasta codigos/arquivos/22.**

**Exibe uma mensagem de sucesso no terminal.**


```python
elif "23" in nome:
    os.rename(f"codigos/arquivos/{nome}", f"codigos/arquivos/23/{nome}")
    print(f"✅ '{nome}' movido para pasta 23 com sucesso.")
```

**Se o nome não contém "22", verifica se contém "23".**

**Move o arquivo para a subpasta codigos/arquivos/23.**

**Exibe uma mensagem de sucesso no terminal.**


```python
except Exception as e:
    print(f"❌ Erro ao mover '{nome}': {e}")
```


**Captura qualquer erro que ocorra dentro do bloco try.**

**Exibe uma mensagem de erro no terminal, informando o nome do arquivo e o motivo da falha.**

---

## ✅ Resultado Final

*Filtra arquivos .txt com "22" ou "23" no nome.*

*Move cada arquivo para sua pasta correspondente.*

*Exibe mensagens de sucesso ou erro para cada operação.*