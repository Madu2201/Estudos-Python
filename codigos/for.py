""" Estrutura de repetição FOR
for i in range(5):
    print("Olá! Tudo bem?")
 """

""" lista_precos = [1500, 1000, 800,2000]

# Percorrendo uma lista e utilizando uma Estrutura de Controle
for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    
    print(f"Preço: {preco}, Imposto: {imposto}") """


# Total de Imposto
lista_precos = [1500, 1000, 800,2000]
total_imposto = 0 # Acumulado
print(f"O total de impostos inicialmente é: {total_imposto}\n")

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    
    print(f"Preço: {preco}, Imposto: {imposto}")
    total_imposto += imposto
    print(f"O total de impostos é: {total_imposto}\n")

print(f"O total de impostos final é: {total_imposto}")