'''
A função input() sempre retorna um valor do tipo string (texto).
Usamos float() para converter esse texto em um número decimal.
'''
vendas = float(input("Digite suas vendas do dia:"))

# Calcula o bônus como 1% do valor das vendas
bonus = vendas * 0.01

# Exibe o valor do bônus calculado
print(f"O seu bônus foi de: R${bonus:.2f}")

