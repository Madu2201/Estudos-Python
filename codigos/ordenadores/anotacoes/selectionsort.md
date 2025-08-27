# Selection Sort em Python

O Selection Sort é um algoritmo de ordenação simples e intuitivo. Ele percorre a lista procurando o menor elemento e o coloca na primeira posição, repetindo esse processo para as próximas posições até que toda a lista esteja ordenada.

---

## Exemplo de Código Selection Sort

```python
def selection_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Selection Sort.

    Parâmetros:
        lista (list): Lista de elementos a serem ordenados (modificada no local).

    Funcionamento:
        - Para cada posição da lista, encontra o menor elemento do restante.
        - Troca o menor elemento encontrado com o elemento da posição atual.
        - Repete até que toda a lista esteja ordenada.
    """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Exemplo de uso
if __name__ == "__main__":
    numeros = [5, 2, 9, 1, 5, 6]
    print("Lista original:", numeros)
    selection_sort(numeros)
    print("Lista ordenada:", numeros)
```

---

## Sobre o Selection Sort

- **Funcionamento:**  
  O algoritmo percorre a lista, encontra o menor elemento e o coloca na posição correta, repetindo esse processo para todas as posições.

- **Vantagens:**  
  - Fácil de entender e implementar.
  - Não depende de estrutura adicional de dados.

- **Desvantagens:**  
  - Ineficiente para listas grandes (complexidade O(n²)).
  - Não recomendado para grandes volumes de dados.

- **Aplicações:**  
  - Ensino de algoritmos de ordenação.
  - Situações onde a simplicidade é mais importante que a performance.

---

## Referência

Veja o código completo e comentado em [`selectionsort.py`](../selectionsort.py)