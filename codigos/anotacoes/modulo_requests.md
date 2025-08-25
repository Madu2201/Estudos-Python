# 📡 Biblioteca requests em Python

A biblioteca requests é uma ferramenta poderosa e fácil de usar para fazer requisições HTTP em Python. Ela permite que você interaja com APIs, baixe conteúdo da web, envie dados e muito mais — tudo com uma sintaxe simples e intuitiva.

[Ver código completo](/codigos/modulos/bibliotecas.py)

---

### 🚀 Instalação

**Para instalar a biblioteca, basta usar o pip:**

```python
bash
pip install requests
```

---

### 📚 Principais Funcionalidades

**1. requests.get(url)**

*Faz uma requisição HTTP do tipo GET para obter dados de uma URL.*

```python
import requests
resposta = requests.get("https://api.exemplo.com/dados")
print(resposta.text)  # Conteúdo bruto da resposta
```


**2. requests.post(url, data=...)**

*Envia dados para uma URL usando o método POST.*

```python
dados = {"nome": "Maria", "idade": 30}
resposta = requests.post("https://api.exemplo.com/usuarios", data=dados)
```


**3. requests.put(url, data=...)**

*Atualiza dados existentes com o método PUT.*


**4. requests.delete(url)**

*Remove dados de um recurso com o método DELETE.*

---

### 🔍 Atributos Importantes da Resposta

**Depois de fazer uma requisição, você pode acessar várias informações:**

| 🧩 Atributo           | 📘 Descrição                                                 |
|----------------------|--------------------------------------------------------------|
| `resposta.status_code` | Código HTTP da resposta (ex: `200` para sucesso, `404` para não encontrado) |
| `resposta.text`        | Conteúdo da resposta como uma string bruta                  |
| `resposta.json()`      | Converte o conteúdo da resposta em um dicionário (formato JSON) |
| `resposta.headers`     | Retorna os cabeçalhos da resposta HTTP                      |
| `resposta.url`         | URL final após redirecionamentos automáticos                |

---

## 🛠️ Exemplos Práticos

**✅ Verificar se a requisição foi bem-sucedida**

```python
if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro:", resposta.status_code)
```

---

### 🌐 Trabalhar com APIs

```python
link = "https://economia.awesomeapi.com.br/last/USD-BRL"
resposta = requests.get(link)
dados = resposta.json()
print("Cotação do dólar:", dados["USDBRL"]["bid"])
```

---


### 🔒 Autenticação

**Você pode enviar credenciais com auth:**

```python
resposta = requests.get("https://api.exemplo.com/segura", auth=("usuario", "senha"))
```

---

## 🧠 Dicas Avançadas

**Use params para enviar parâmetros na URL:**

```python
requests.get("https://api.exemplo.com/busca", params={"q": "python"})
```


**Use headers para customizar cabeçalhos:**

```python
requests.get("https://api.exemplo.com", headers={"User-Agent": "MeuApp"})
```


**Use timeout para evitar travamentos:**

```python
requests.get("https://api.exemplo.com", timeout=5)
```

---

## 📎 Documentação Oficial

Para mais detalhes, consulte: https://docs.python-requests.org