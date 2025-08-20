vendas_22 = {
            "jan": 15000, 
            "fev": 15500, 
            "mar": 14000, 
            "abr": 16600, 
            "mai": 16300,
            "jun": 17000
            }

vendas_23 = {
            "jan": 17000, 
            "fev": 15000, 
            "mar": 17500, 
            "abr": 16900, 
            "mai": 16000,
            "jun": 18500
            }

# 1° Saber quanto variou percentualmente cada mês de 2023 comparado com 2022

for mes in vendas_23:  # Itera sobre cada mês presente no dicionário vendas_23 (as chaves são os nomes dos meses)
    valor_22 = vendas_22[mes]  # Recupera o valor de vendas do mesmo mês em 2022
    valor_23 = vendas_23[mes]  # Recupera o valor de vendas do mês em 2023

    # Calcula a variação percentual entre os dois anos
    var_percentual = valor_23 / valor_22 - 1

    # Exibe a variação percentual formatada como porcentagem com uma casa decimal
    print(f"Variação do {mes}: {var_percentual: .1%}")


# 2° Simular: Se a empresa tivesse pelo menos empatado com 2022 nos meses em que vendeu menos, qual seria o faturamento

fat_total_simulado = 0  # Inicializa o faturamento total simulado

for mes in vendas_23:  # Itera sobre cada mês presente no dicionário vendas_23
    valor_22 = vendas_22[mes]  # Recupera o valor de vendas do mesmo mês em 2022
    valor_23 = vendas_23[mes]  # Recupera o valor de vendas do mês em 2023
    var_percentual = valor_23 / valor_22 - 1  # Calcula a variação percentual

    # Se o valor de 2023 for menor que o de 2022, considera o valor de 2022 (simulando empate)
    if valor_23 < valor_22:
        fat_total_simulado += valor_22
    else:
        fat_total_simulado += valor_23  # Caso contrário, mantém o valor real de 2023

    # Exibe a variação percentual do mês
    print(f"Variação do {mes}: {var_percentual: .1%}")

# Exibe o faturamento total simulado considerando os empates nos meses de queda
print(f"Faturamento total simulado: R$ {fat_total_simulado:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

