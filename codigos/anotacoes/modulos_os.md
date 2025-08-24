# 📦 Módulo os no Python

O módulo os permite que o Python interaja com o sistema operacional. Com ele, é possível manipular arquivos, pastas, caminhos, variáveis de ambiente e até executar comandos no terminal.

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

---

## 📂 Criar pastas

```python
os.mkdir("nova_pasta")               # Cria uma pasta
os.makedirs("pasta/subpasta")        # Cria estrutura de pastas
```

---

## 🗑️ Remover pastas

```python
os.rmdir("pasta")                   # Remove pasta vazia
os.removedirs("pasta/subpasta")     # Remove estrutura de pastas vazias
```

---

## 🔄 Renomear ou mover arquivos

```python
os.rename("origem.txt", "destino.txt")
```

*Move ou renomeia um arquivo ou pasta.*

---

## ❌ Remover arquivos

```python
os.remove("arquivo.txt")
```

---

## 📌 Navegação e Caminhos

**📍 Diretório atual**

```python
os.getcwd()
```

*Retorna o caminho do diretório atual.*

---

## 🚶‍♀️ Mudar de diretório

```python
os.chdir("novo_diretorio")
```

---

## 🔗 Construir caminhos seguros

```python
os.path.join("pasta", "arquivo.txt")
```

*Evita erros com separadores de caminho (/ ou \).*

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

---

## 🌍 Variáveis de Ambiente

**🔎 Acessar variáveis**

```python
os.environ["USER"]
os.getenv("PATH")
```

---

## 🖥️ Informações do Sistema

```python
os.name        # Retorna 'posix' (Linux/macOS) ou 'nt' (Windows)
```

---

## ⚙️ Executar comandos do sistema

```python
os.system("echo Olá, mundo!")
```

*Executa um comando no terminal.*

---

# 🧹 Boas práticas

**Use os.path.join() para montar caminhos de forma segura.**

**Combine com o módulo shutil para copiar arquivos e pastas.**

**Evite os.system() quando possível — prefira subprocess para mais controle.**