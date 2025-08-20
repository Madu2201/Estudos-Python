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