# 📘 Funções em Python:

### 🧮 Função `sum()`

A função `sum()` é usada para somar todos os elementos de um iterável (como listas, tuplas ou conjuntos).

#### 📌 Sintaxe:
```python
sum(iterável, início)

- `iterável`:  qualquer objeto que possa ser percorrido (como uma lista de números).
- `início (opcional)`: valor inicial da soma. Se fornecido, será adicionado ao total.

- Exemplo¹
numeros = [1, 2, 3, 4]
print(sum(numeros))  # Saída: 10

# Soma com valor inicial
print(sum(numeros, 10))  # Saída: 20
```

### 🔧 Outras funções úteis em Python

*Função*	    *Descrição*
`len()`	        Retorna o número de itens em um objeto (como lista, string, etc.)

`max()`	        Retorna o maior valor de um iterável

`min()`	        Retorna o menor valor de um iterável

`sorted()`	    Retorna uma lista ordenada a partir de um iterável

`enumerate()`   Retorna pares (índice, valor) ao iterar sobre uma sequência

`zip()`	        Junta múltiplas listas em pares (ou tuplas) correspondentes

`map()`	        Aplica uma função a cada item de um iterável

`filter()`	    Filtra itens de um iterável com base em uma função que retorna True
