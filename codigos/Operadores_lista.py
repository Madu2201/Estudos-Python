# Operadores em listas Python

# Operador '+' (concatenação)
lista1 = [1, 2, 3]
lista2 = [4, 5]
lista3 = lista1 + lista2  # Junta as duas listas
print("Concatenação (+):", lista3)  # [1, 2, 3, 4, 5]

# Operador '*' (repetição)
lista4 = [0, 1]
lista5 = lista4 * 3  # Repete a lista 3 vezes
print("Repetição (*):", lista5)  # [0, 1, 0, 1, 0, 1]

# Operador 'in' (verificação de existência)
print(2 in lista1)  # True, verifica se 2 está em lista1

# Operador 'not in' (verificação de ausência)
print(10 not in lista2)  # True, verifica se 10 não está em lista2

# Operador 'len' (tamanho da lista)
print("Tamanho da lista1:", len(lista1))  # 3, lista1 tem 3 elementos
print("Tamanho da lista2:", len(lista2))  # 2, lista2 tem 2 elementos

# Operador de fatiamento (slicing)
lista6 = lista3[1:4]  # Obtém uma fatia da lista3 do índice 1 ao 3
print("Fatiamento (slicing):", lista6)  # [2, 3, 4]

# Operador de atribuição em múltiplas variáveis
a, b, c = lista1  # Atribui os valores da lista1 às variáveis a, b e c
print("Atribuição múltipla:", a, b, c)  # 1 2 3

# Operador de repetição com fatiamento
lista7 = lista1[:2] * 2  # Repete a fatia da lista1 do início até o índice 2
print("Repetição com fatiamento:", lista7)  # [1, 2, 1, 2]

# Operador de verificação de igualdade
print(lista1 == [1, 2, 3])  # True, verifica se lista1 é igual a [1, 2, 3]

# Operador de verificação de identidade
# True, verifica se lista1 é o mesmo objeto que a fatia da lista3
print(lista1 is lista3[:3])
