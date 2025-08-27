# Insertion Sort em Python

O Insertion Sort é um algoritmo de ordenação simples e eficiente para listas pequenas. Ele percorre a lista, inserindo cada elemento na posição correta em relação aos anteriores, como se estivesse organizando cartas na mão.

---

## Exemplo de Código Insertion Sort

```python
def insertion_sort(lista):
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        chave = lista[i]  # Elemento a ser inserido
        j = i - 1
        # Move os elementos maiores que a chave para frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave  # Insere a chave na posição correta
    return lista

# Exemplo de uso
if __name__ == "__main__":
    numeros = [5, 2, 9, 1, 5, 6]
    print("Lista original:", numeros)
    ordenada = insertion_sort(numeros)
    print("Lista ordenada:", ordenada)
```

---

## Sobre o Insertion Sort

- **Funcionamento:**  
  O algoritmo percorre a lista e insere cada elemento na posição correta entre os anteriores, deslocando os maiores para frente.

- **Vantagens:**  
  - Simples de implementar.
  - Muito eficiente para listas pequenas ou quase ordenadas.

- **Desvantagens:**  
  - Não recomendado para listas grandes (complexidade O(n²)).

- **Aplicações:**  
  - Ordenação de pequenas quantidades de dados.
  - Situações onde a lista já está quase ordenada.

---

## Referência

Veja o código completo e comentado em [`insertionsort.py`](../insertionsort.py).