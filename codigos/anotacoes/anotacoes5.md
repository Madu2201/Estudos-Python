# 🐍 Operadores em Python

Este documento apresenta os principais operadores disponíveis na linguagem Python, organizados por categoria, com exemplos e explicações.

---

## 🔢 Operadores Aritméticos

Usados para realizar operações matemáticas básicas.

| Operador | Descrição       | Exemplo        | Resultado |
|----------|------------------|----------------|-----------|
| `+`      | Adição           | `2 + 3`        | `5`       |
| `-`      | Subtração        | `5 - 2`        | `3`       |
| `*`      | Multiplicação    | `4 * 3`        | `12`      |
| `/`      | Divisão          | `10 / 2`       | `5.0`     |
| `//`     | Divisão inteira  | `10 // 3`      | `3`       |
| `%`      | Módulo (resto)   | `10 % 3`       | `1`       |
| `**`     | Exponenciação    | `2 ** 3`       | `8`       |

---

## 🧮 Operadores de Comparação

Comparam valores e retornam `True` ou `False`.

| Operador | Descrição             | Exemplo        | Resultado |
|----------|------------------------|----------------|-----------|
| `==`     | Igualdade              | `5 == 5`       | `True`    |
| `!=`     | Diferença              | `5 != 3`       | `True`    |
| `>`      | Maior que              | `5 > 3`        | `True`    |
| `<`      | Menor que              | `2 < 4`        | `True`    |
| `>=`     | Maior ou igual         | `5 >= 5`       | `True`    |
| `<=`     | Menor ou igual         | `3 <= 4`       | `True`    |

---

## 🔀 Operadores Lógicos

Usados para combinar expressões booleanas.

| Operador | Descrição        | Exemplo                  | Resultado |
|----------|------------------|--------------------------|-----------|
| `and`    | E lógico         | `True and False`         | `False`   |
| `or`     | OU lógico        | `True or False`          | `True`    |
| `not`    | Negação lógica   | `not True`               | `False`   |

---

## 📦 Operadores de Atribuição

Atribuem valores a variáveis, podendo combinar com operadores aritméticos.

| Operador | Exemplo     | Equivalente a     |
|----------|-------------|-------------------|
| `=`      | `x = 5`     | Atribuição simples|
| `+=`     | `x += 3`    | `x = x + 3`       |
| `-=`     | `x -= 2`    | `x = x - 2`       |
| `*=`     | `x *= 4`    | `x = x * 4`       |
| `/=`     | `x /= 2`    | `x = x / 2`       |
| `//=`    | `x //= 2`   | `x = x // 2`      |
| `%=`     | `x %= 3`    | `x = x % 3`       |
| `**=`    | `x **= 2`   | `x = x ** 2`      |

---

## 📚 Operadores de Identidade

Verificam se duas variáveis apontam para o mesmo objeto.

| Operador | Descrição         | Exemplo         | Resultado |
|----------|-------------------|-----------------|-----------|
| `is`     | Mesmo objeto       | `x is y`        | `True/False` |
| `is not` | Objetos diferentes | `x is not y`    | `True/False` |

---

## 📦 Operadores de Associação (Membership)

Verificam se um valor está presente em uma sequência (lista, string, etc).

| Operador | Descrição         | Exemplo           | Resultado |
|----------|-------------------|-------------------|-----------|
| `in`     | Está contido      | `'a' in 'Maria'`  | `True`    |
| `not in` | Não está contido  | `3 not in [1,2]`  | `True`    |

---

## ⚙️ Operadores Bitwise

Operam diretamente sobre os bits dos números inteiros.

| Operador | Descrição       | Exemplo     | Resultado |
|----------|------------------|-------------|-----------|
| `&`      | AND bit a bit    | `5 & 3`     | `1`       |
| `|`      | OR bit a bit     | `5 | 3`     | `7`       |
| `^`      | XOR bit a bit    | `5 ^ 3`     | `6`       |
| `~`      | NOT bit a bit    | `~5`        | `-6`      |
| `<<`     | Shift à esquerda | `5 << 1`    | `10`      |
| `>>`     | Shift à direita  | `5 >> 1`    | `2`       |

---

## 🧠 Dica Final

Você pode usar a função `type()` para verificar o tipo de resultado de uma operação:

```python
print(type(10 / 2))  # <class 'float'>
print(type(10 // 2)) # <class 'int'>
