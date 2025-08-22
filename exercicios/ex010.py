# Cria uma lista com nomes de frutas
lista = ["maça", "uva", "banana"]

# Percorre cada fruta na lista
for fruta in lista:
    # Inicializa o contador de letras da fruta atual
    qtdeLetras = 0

    # Percorre cada letra da fruta
    for letras in fruta:
        # Incrementa o contador de letras
        qtdeLetras += 1

    # Exibe o nome da fruta com a primeira letra maiúscula
    # e a quantidade de letras que ela possui
    print(f"Fruta: {fruta.capitalize()}\nQuantidade de letras = {qtdeLetras}")
