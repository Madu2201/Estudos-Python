faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # Operação de adição
imposto = faturamento * 0.15 # Operação de multiplicação
lucro = faturamento - custo - imposto # Operação de subtração

margem_lucro = lucro / faturamento # Operação de divisão

'''
print(f"Faturamento: {faturamento}")
print(f"Custo: {custo}")
print(f"Novas Vendas: {novas_vendas}")
print(f"Imposto: {imposto}")
print(f"Lucro: {lucro}")
print(f"Margem de Lucro: {margem_lucro:.2%}") # Formatação de porcentagem, com duas casas decimais e símbolo de porcentagem
print(f"Faturamento após novas vendas: {faturamento + novas_vendas}")

'''

''' 
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12) # Transformação de tipo para inteiro
print(f"Tempo em anos: {tempo_em_anos}") # Exibe o tempo em anos
print(f"Tempo em meses: {tempo_em_meses % 12}") # Operação de módulo que calcula o restante da divisão por 12
print(f"Tempo total: {tempo_em_anos} anos e {tempo_em_meses % 12} meses") # Exibe o tempo total em anos e meses

'''

numero = 123.57
print (f"Arredondamento: {round(numero)}") # Arredonda o número para o inteiro mais próximo
print (f"Arredondamento com duas casas decimais: {round(numero, 2)}") # Arredonda o número para duas casas decimais

faturamento = 139_018_182 # Utiliza o separador de milhar para facilitar a leitura do número
