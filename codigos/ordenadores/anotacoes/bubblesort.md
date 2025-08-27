# Bubble Sort em Python

O Bubble Sort é um algoritmo de ordenação simples e didático. Ele percorre a lista várias vezes, comparando elementos adjacentes e trocando-os de posição se estiverem fora de ordem. O maior elemento "flutua" para o final da lista a cada passagem, como uma bolha subindo na água.

---

## Exemplo de Código Bubble Sort

```python
def bubble_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Bubble Sort.

    Parâmetros:
        lista (list): Lista de elementos a serem ordenados (modificada no local).

    Funcionamento:
        - Percorre a lista várias vezes.
        - Em cada passagem, compara pares de elementos adjacentes.
        - Se estiverem fora de ordem, troca de posição.
        - Repete até que toda a lista esteja ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Exemplo de uso
if __name__ == "__main__":
    numeros = [5, 2, 9, 1, 5, 6]
    print("Lista original:", numeros)
    bubble_sort(numeros)
    print("Lista ordenada:", numeros)
```

---

## Sobre o Bubble Sort

- **Funcionamento:**  
  O algoritmo compara pares de elementos adjacentes e os troca de posição se estiverem na ordem errada. Esse processo é repetido até que toda a lista esteja ordenada.

- **Vantagens:**  
  - Fácil de entender e implementar.
  - Bom para listas pequenas ou para fins didáticos.

- **Desvantagens:**  
  - Ineficiente para listas grandes (complexidade O(n²)).
  - Não recomendado para grandes volumes de dados.

- **Aplicações:**  
  - Ensino de algoritmos de ordenação.
  - Situações onde a simplicidade é mais importante que a performance.

---

## Referência

Veja o código completo e comentado em [`bubblesort.py`](../bubblesort.py).