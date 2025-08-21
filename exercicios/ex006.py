# Dicionário com os vendedores e suas vendas
vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180]
}

# Função que calcula o bônus total de um vendedor
def calcular_bonus(lista_vendas):
    quantidade = len(lista_vendas)       # Conta quantas vendas foram feitas
    bonus1 = quantidade * 2              # R$2 por venda
    valor_total = sum(lista_vendas)      # Soma das vendas
    bonus2 = 0.01 * valor_total          # 1% do valor total
    bonus = bonus1 + bonus2              # Bônus total

    return bonus

bonus_tot = 0                            # Total geral de bônus

# Loop para calcular e mostrar o bônus de cada vendedor
for vendedor, lista_vendas_vendedor in vendas.items():
    bonus = calcular_bonus(lista_vendas_vendedor) # Calcula o bônus do vendedor
    print(f"Vendedor: {vendedor}, Bonus: {bonus: .2f}\n")
    bonus_tot += bonus # Soma ao total de bônus pagos

# Exibe o total de bônus pagos
print(f"O bonus total: {bonus_tot}")

# Trecho comentado para mostrar como acessar os dados do dicionário
# print(vendas.items())  # Mostra os pares (vendedor, lista de vendas)
