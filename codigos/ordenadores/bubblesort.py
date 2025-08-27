# Algoritmo Bubble Sort em Python
# O Bubble Sort é um algoritmo de ordenação simples que compara pares de elementos adjacentes
# e os troca de posição se estiverem na ordem errada. Esse processo é repetido até que a lista esteja ordenada.

def bubble_sort(lista):
    n = len(lista)
    # Percorre toda a lista
    for i in range(n):
        # Para cada elemento, compara com o próximo
        for j in range(0, n - i - 1):
            # Se o elemento atual for maior que o próximo, troca de posição
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Exemplo de uso
if __name__ == "__main__":
    numeros = [5, 2, 9, 1, 5, 6]
    print("Lista original:", numeros)
    bubble_sort(numeros)
    print("Lista ordenada:", numeros)