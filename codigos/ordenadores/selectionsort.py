# Algoritmo Selection Sort em Python

def selection_sort(arr):
    # Para cada posição, encontra o menor elemento do restante e troca
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    numeros = [64, 25, 12, 22, 11]
    print("Lista original:", numeros)
    selection_sort(numeros)
    print("Lista ordenada:", numeros)
