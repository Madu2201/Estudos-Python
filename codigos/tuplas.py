# Função para calcular três tipos de impostos sobre um preço
def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir       # Calcula o imposto de renda
    imposto_csll = preco * csll   # Calcula o CSLL
    imposto_iss = preco * iss     # Calcula o ISS
    return imposto_ir, imposto_csll, imposto_iss  # Retorna os três valores como uma tupla

# Chamada da função com preço fixo de 1000
ir, csll, iss = calcular_imposto2(1000)  # Unpacking: atribui cada valor da tupla a uma variável

# Exibe os valores dos impostos, um por linha
print(ir, csll, iss, sep="\n")  # sep="\n" faz com que cada valor seja impresso em uma linha separada
