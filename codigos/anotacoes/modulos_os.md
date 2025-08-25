# 📦 Módulo os no Python

O módulo os permite que o Python interaja com o sistema operacional. Com ele, é possível manipular arquivos, pastas, caminhos, variáveis de ambiente e até executar comandos no terminal.

[Ver código completo](/codigos/modulos/bibliotecas.py)

---

## 🔹 Importação

```python
import os
```

---

## 📁 Manipulação de Arquivos e Diretórios

**🔍 Listar conteúdo de uma pasta**
```python
os.listdir("caminho/da/pasta")
```
*Retorna uma lista com os nomes de arquivos e subpastas.*

### EXEMPLO

```python
arquivos = os.listdir("meus_dados")
print(arquivos)
```

*Retorna uma lista com os nomes de arquivos e subpastas dentro de meus_dados.*

---

## 📂 Criar pastas

```python
os.mkdir("nova_pasta")               # Cria uma pasta
os.makedirs("pasta/subpasta")        # Cria estrutura de pastas
```

### EXEMPLO

```python
os.mkdir("relatorios")  # Cria uma pasta chamada 'relatorios'
os.makedirs("relatorios/2025/agosto")  # Cria estrutura de subpastas
```

---

## 🗑️ Remover pastas

```python
os.rmdir("pasta")                   # Remove pasta vazia
os.removedirs("pasta/subpasta")     # Remove estrutura de pastas vazias
```

### EXEMPLO

```python
os.rmdir("relatorios")  # Remove a pasta se estiver vazia
os.removedirs("relatorios/2025/agosto")  # Remove todas as pastas se estiverem vazias
```

---

## 🔄 Renomear ou mover arquivos

```python
os.rename("origem.txt", "destino.txt")
```

*Move ou renomeia um arquivo ou pasta.*

### EXEMPLO

```python
os.rename("dados.txt", "arquivos/dados_renomeado.txt")
```

*Move o arquivo dados.txt para a pasta arquivos com um novo nome.*

---

## ❌ Remover arquivos

```python
os.remove("arquivo.txt")
```

### EXEMPLO

```python
os.remove("arquivos/dados_renomeado.txt")
```

*Apaga o arquivo especificado.*

---

## 📌 Navegação e Caminhos

**📍 Diretório atual**

```python
os.getcwd()
```

*Retorna o caminho do diretório atual.*

### EXEMPLO

```python
print(os.getcwd())
```

*Mostra o caminho da pasta onde o script está sendo executado.*

---

## 🚶‍♀️ Mudar de diretório

```python
os.chdir("novo_diretorio")
```

*Muda o diretório de trabalho para a pasta*

---

## 🔗 Construir caminhos seguros

```python
os.path.join("pasta", "arquivo.txt")
```

*Evita erros com separadores de caminho (/ ou \).*

### EXEMPLO

```python
caminho = os.path.join("relatorios", "agosto", "dados.txt")
print(caminho)
```

*Cria um caminho seguro, independente do sistema operacional.*

---

## 🧪 Verificações

**✅ Verificar se um caminho existe**

```python
os.path.exists("caminho")
```

---

## 📄 Verificar se é arquivo ou pasta

```python
os.path.isfile("arquivo.txt")
os.path.isdir("pasta")
```

### EXEMPLO¹

```python
if os.path.exists("relatorios/agosto"):
    print("Pasta encontrada!")
```

*Verifica se um caminho existe*

### EXEMPLO²

```python
print(os.path.isfile("dados.txt"))  # True se for arquivo
print(os.path.isdir("relatorios"))  # True se for pasta
```

*Verificar se é arquivo ou pasta*

---

## 🌍 Variáveis de Ambiente

**🔎 Acessar variáveis**

```python
os.environ["USER"]
os.getenv("PATH")
```

### EXEMPLO

```python
usuario = os.environ.get("USERNAME")
print(f"Usuário atual: {usuario}")
```

*Acessa variáveis*

---

## 🖥️ Informações do Sistema

```python
os.name        # Retorna 'posix' (Linux/macOS) ou 'nt' (Windows)
```

### EXEMPLO

```python
print(os.name)  # 'nt' para Windows, 'posix' para Linux/macOS
```

---

## ⚙️ Executar comandos do sistema

```python
os.system("echo Olá, mundo!")
```

*Executa um comando no terminal.*

### EXEMPLO

```python
os.system("echo Olá, Maria!")
```

*Executa um comando no terminal.*

---

# 🧹 Boas práticas

**Use os.path.join() para montar caminhos de forma segura.**

**Combine com o módulo shutil para copiar arquivos e pastas.**

**Evite os.system() quando possível — prefira subprocess para mais controle.**