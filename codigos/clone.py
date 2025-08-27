# Exemplo de clonagem de listas em Python

lista_original = [1, 2, 3, 4]

# Clonando usando '=' (referência, NÃO é cópia de verdade)
lista_a = lista_original
lista_a.append(5)
print("Usando '=':", lista_original)  # Altera também a original

# Clonando usando ':' (slice, cópia superficial)
lista_b = lista_original[:]
lista_b.append(6)
print("Usando slice ':' :", lista_original)  # Não altera a original
print("Lista clonada com slice:", lista_b)

# Clonando usando copy() (cópia superficial)
lista_c = lista_original.copy()
lista_c.append(7)
print("Usando copy():", lista_original)  # Não altera a original
print("Lista clonada com copy():", lista_c)
