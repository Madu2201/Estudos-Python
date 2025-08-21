vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180]
}

# Cada venda o vendedor ganha R$2 e 1% do valor da venda
# Calcular o valor total de bonus pago e o bonus de cada vendedor

def calcular_bonus(lista_vendas):
    quantidade = len(lista_vendas)
    bonus1 = quantidade * 2
    valor_total = sum(lista_vendas)
    bonus2 = 0.01 * valor_total
    bonus = bonus1 + bonus2

    return bonus

bonus_tot = 0

for vendedor, lista_vendas_vendedor  in vendas.items():
    bonus = calcular_bonus(lista_vendas_vendedor)
    print(f"Vendedor: {vendedor}, Bonus: {bonus: .2f}\n")
    bonus_tot += bonus

print(f"O bonus total: {bonus_tot}")

""" print(vendas.items()) # Transforma o dicionário em uma lista de tuplas

for vendedor, lista_vendas in vendas.items(): # Fazendo unpacking dessa Tupla automaticamente
    print(vendedor)
    print(lista_vendas) """
