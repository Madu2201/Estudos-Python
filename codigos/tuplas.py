def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    # Retorna os três valores de imposto como uma tupla
    return imposto_ir, imposto_csll, imposto_iss

# Chamada da função com preço fixo de 1000
ir, csll, iss = calcular_imposto2(1000)

# Exibe a tupla com os três impostos calculados, que nada mais é que uma lista entre parênteses
# Uma tupla () é imutável, ou seja, pq vc não consegue mudar o valor dela.
# Resultado esperado: (275.0, 35.0, 50.0)
#print(resposta)
#print(resposta[0])

#ir,csll, iss = resposta # Unpacking, ou seja, atribuindo os valores as variáveis, o 1 valor na 1 variável e assim por diante.

print(ir, csll, iss, sep="\n") # sep= signinifica qual vai ser o separador no print