faturamento = 1200
custo = 770

novas_vendas = 300
faturamento += novas_vendas

taxa_imposto = 0.1 # 10% de imposto
imposto = faturamento * taxa_imposto 

print(f"O faturamento atual é de {faturamento}") 
print (f"O custo atual é de {custo}") 
print (f"O lucro atual é de {faturamento - custo - imposto}")