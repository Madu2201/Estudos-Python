# Lista com os preços dos produtos
lista_precos = [1500, 1000, 800, 2000]

# Variável que acumula o total de impostos calculados
total_imposto = 0
print(f"O total de impostos inicialmente é: {total_imposto}\n")

# Função que calcula o imposto com base no preço do produto
# Recebe como argumentos: o preço, a alíquota para preços acima de 1000 (aliquota1),
# e a alíquota para preços iguais ou abaixo de 1000 (aliquota2)
# As alíquotas têm valores padrão, caso não sejam informadas na chamada da função
def calcular_imposto(preco, aliquota1=0.2, aliquota2=0.1):
    # Verifica se o preço é maior que 1000 para aplicar a alíquota correspondente
    if preco > 1000:
        imposto = preco * aliquota1
    else:
        imposto = preco * aliquota2
    # Exibe o preço e o imposto calculado
    print(f"Preço: {preco}, Imposto: {imposto}")
    # Retorna o valor do imposto para ser usado fora da função
    return imposto

# Loop que percorre cada preço na lista
for preco in lista_precos:
    # Chama a função passando o preço e uma alíquota personalizada para preços altos
    imposto = calcular_imposto(preco, aliquota1=0.25)
    # Soma o imposto calculado ao total acumulado
    total_imposto += imposto
    # Exibe o total de impostos acumulado até o momento
    print(f"O total de impostos é: {total_imposto}\n")

# Exibe o total final de impostos após o loop
print(f"O total de impostos final é: {total_imposto}\n")

# Função que calcula três tipos de impostos sobre um preço:
# IR (Imposto de Renda), CSLL (Contribuição Social sobre o Lucro Líquido), e ISS (Imposto sobre Serviços)
# Cada imposto tem uma alíquota padrão, mas pode ser alterada na chamada da função
def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    # Retorna os três valores de imposto como uma tupla
    return imposto_ir, imposto_csll, imposto_iss

# Chamada da função com preço fixo de 1000
resposta = calcular_imposto2(1000)

# Exibe a tupla com os três impostos calculados
# Resultado esperado: (275.0, 35.0, 50.0)
print(resposta)
