# Funções de Ordenação em Python: `sort()` e `sorted()`

Em Python, existem duas formas principais de ordenar listas: usando o método `sort()` e a função `sorted()`. Ambas permitem ordenar elementos em ordem crescente ou decrescente, mas possuem diferenças importantes.

---

## Exemplo de Código

```python
# Lista de números
numeros = [5, 2, 9, 1, 7]

# Usando sorted(): retorna uma nova lista ordenada, não altera a original
numeros_ordenados = sorted(numeros)
print("Lista original:", numeros)
print("Lista ordenada com sorted():", numeros_ordenados)

# Usando sort(): ordena a lista original "in-place" (sem criar nova lista)
numeros.sort()
print("Lista após sort():", numeros)

# Ambos aceitam o parâmetro reverse=True para ordem decrescente
decrescente_sorted = sorted(numeros, reverse=True)
print("Ordenada decrescente com sorted():", decrescente_sorted)

numeros.sort(reverse=True)
print("Ordenada decrescente com sort():", numeros)
```

---

## Diferenças entre `sort()` e `sorted()`

| Função/Método | O que faz?                              | Altera a lista original? | Retorna nova lista? | Parâmetro `reverse` |
|---------------|-----------------------------------------|-------------------------|---------------------|---------------------|
| `sort()`      | Ordena a lista "in-place"               | Sim                     | Não                 | Sim                 |
| `sorted()`    | Retorna uma nova lista ordenada         | Não                     | Sim                 | Sim                 |

---

## Dicas

- Use `sorted()` quando quiser manter a lista original intacta.
- Use `sort()` para economizar memória e ordenar diretamente a lista.
- Ambos aceitam o parâmetro `reverse=True` para ordenar em ordem decrescente.
- Também é possível ordenar listas de strings, tuplas e objetos usando o parâmetro `key`.

---

## Referência

Veja o código completo e comentado em [`sorted_sort.py`](../sorted_sort.py).