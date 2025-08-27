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
