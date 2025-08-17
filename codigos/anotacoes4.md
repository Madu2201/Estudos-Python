# 📘 Funções em Python:

### 🧮 Função `sum()`

A função `sum()` é usada para somar todos os elementos de um iterável (como listas, tuplas ou conjuntos).

#### 📌 Sintaxe:
```python
sum(iterável, início)

- `iterável`:  qualquer objeto que possa ser percorrido (como uma lista de números).
- `início (opcional)`: valor inicial da soma. Se fornecido, será adicionado ao total.

- Exemplo¹:
```
numeros = [1, 2, 3, 4]
print(sum(numeros))  # Saída: 10

# Soma com valor inicial
print(sum(numeros, 10))  # Saída: 20
```