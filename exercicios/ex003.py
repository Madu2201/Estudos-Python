# Solicita ao usuário que digite o valor total de vendas
vendas = int(input("Digite o valor total de vendas: "))

# Lista com os valores de bônus para diferentes faixas de vendas
bonus = [500, 250, 100]  # índice 0: maior bônus, índice 2: menor bônus

# Verifica se as vendas estão entre 5.000 e 9.999
if 5000 <= vendas <= 9999:
    vendas += bonus[2]  # adiciona o bônus de R$100
    print(f"Parabéns! você ganhou um bônus de R${bonus[2]:.2f}, seu salário é de R${vendas:.2f}")

# Verifica se as vendas estão entre 10.000 e 14.999
elif 10000 <= vendas <= 14999:
    vendas += bonus[1]  # adiciona o bônus de R$250
    print(f"Parabéns! você ganhou um bônus de R${bonus[1]:.2f}, seu salário é de R${vendas:.2f}")

# Verifica se as vendas são iguais ou superiores a 15.000
elif vendas >= 15000:
    vendas += bonus[0]  # adiciona o bônus de R$500
    print(f"Parabéns! você ganhou um bônus de R${bonus[0]:.2f}, seu salário é de R${vendas:.2f}")

# Se nenhuma das condições acima for verdadeira (vendas abaixo de 5.000)
else:
    print("Opa, não atingiu o limite de vendas!")

