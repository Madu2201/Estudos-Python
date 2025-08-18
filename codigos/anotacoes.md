# 🧠 Tipos de Dados em Python

Python possui diversos tipos de dados nativos que permitem representar diferentes tipos de informação. Abaixo estão os principais:

---

## 🔢 Numéricos

- **Inteiros (`int`)**: Números sem parte decimal.
  - Exemplos: `1`, `2`, `3`, `-10`, `-50`

- **Decimais (`float`)**: Números com ponto flutuante.
  - Exemplos: `1.5`, `0.75`, `-10.99`

---

## 📝 Texto

- **Strings (`str`)**: Sequência de caracteres.
  - Exemplos: `"Olá"`, `'Mundo'`, `'1234'`

---

## ✅ Booleanos

- **Booleanos (`bool`)**: Representam valores lógicos.
  - Exemplos: `True`, `False`

---

## 📦 Coleções

### 🔹 Listas (`list`)
- Coleção ordenada e mutável.
- Exemplos:
  - `[1, 2, 3]`
  - `['a', 'b', 'c']`
  - `[1, 'a', True]`

### 🔹 Tuplas (`tuple`)
- Coleção ordenada e **imutável**.
- Exemplos:
  - `(1, 2)`
  - `('a', 'b')`
  - `(1, 'a', True)`

### 🔹 Conjuntos (`set`)
- Coleção **não ordenada** e **sem elementos duplicados**.
- Exemplos:
  - `{1, 2, 3}`
  - `{'a', 'b', 'c'}`

### 🔹 Dicionários (`dict`)
- Coleção de pares `chave: valor`.
- Exemplos:
  - `{'chave': 'valor'}`
  - `{'nome': 'João', 'idade': 30}`

---

## 🚫 Tipo Nulo

- **NoneType (`None`)**: Representa a ausência de valor.
  - Exemplo: `None`

---

### Sobre os comentários

- Comentários em Python são feitos com `#` para uma linha ou com aspas triplas `'''` para múltiplas linhas.
- Servem para explicar o funcionamento do código, facilitar o entendimento e registrar observações importantes.

---

## 🧪 Dica Extra

Você pode verificar o tipo de qualquer valor usando a função `type()`:

```python
print(type(3))           # <class 'int'>
print(type("Python"))    # <class 'str'>
print(type([1, 2, 3]))    # <class 'list'>
print(type(None))        # <class 'NoneType'>
