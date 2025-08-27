# Exemplo simples e documentado do uso de sort() e sorted() em Python

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