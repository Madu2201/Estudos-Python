# 🧮 Introdução ao NumPy

**NumPy** é uma biblioteca do Python usada para fazer cálculos matemáticos com mais rapidez e eficiência. Ela é muito usada em ciência de dados, estatística, engenharia e inteligência artificial.

---

## ✅ Por que usar NumPy?

- Trabalha com **arrays** (listas de números) de forma rápida
- Permite fazer **operações matemáticas** sem precisar de loops
- Tem várias **funções prontas** para estatística, álgebra linear e mais

---

## 🔧 Exemplos básicos

```python
import numpy as np
```

```python
# Criando um array
a = np.array([1, 2, 3, 4])
```

```python
# Soma de todos os elementos
print(np.sum(a))  # 10
```

```python
# Média dos valores
print(np.mean(a))  # 2.5
```

```python
# Multiplicando todos os valores por 2
print(a * 2)  # [2 4 6 8]
```

---

## 📦 Funções úteis

**np.array()** → cria um array

**np.sum()** → soma os valores

**np.mean()** → calcula a média

**np.max()** → mostra o maior valor

**np.min()** → mostra o menor valor


# 🔁 Manipulação de Arrays

### `np.reshape()` → muda o formato do array

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape((2, 3))  # transforma em matriz 2x3
print(b)
```

### `np.transpose()` → transposta de uma matriz

```python
matriz = np.array([[1, 2], [3, 4]])
print(np.transpose(matriz))  # [[1 3] [2 4]]
```

### `np.concatenate()` → junta arrays

```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate((a, b)))  # [1 2 3 4]
```

---

## 🔍 Indexação e Fatiamento

Você pode acessar partes de um array como faria com listas:

```python
a = np.array([10, 20, 30, 40])
print(a[1])     # 20
print(a[1:3])   # [20 30]
```

---

## 🎲 Gerando Números Aleatórios

- `np.random.rand()` → números aleatórios entre 0 e 1

```python
print(np.random.rand(3))  # ex: [0.12 0.87 0.45]
```

- `np.random.randint()` → inteiros aleatórios

```python
print(np.random.randint(1, 10, size=5))  # ex: [3 7 2 9 1]
```

---

## 📐 Operações com Matrizes

- `np.dot()` → produto escalar ou multiplicação de matrizes

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))
```

- `np.linalg.inv()` → inversa de uma matriz

```python
matriz = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(matriz))
```