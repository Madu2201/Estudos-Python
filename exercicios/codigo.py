faturamento = 1200
custo = 770

novas_vendas = 300
faturamento += novas_vendas

taxa_imposto = 0.1 # 10% de imposto, escreve-se de forma decimal

'''
números inteiros(int): 1, 2, 3, -10, -50
números decimais (float): 1.5, 0.75, -10.99
strings (str): "Olá", 'Mundo', '1234'
booleanos (bool): True, False
listas (list): [1, 2, 3], ['a', 'b', 'c'], [1, 'a', True]
dicionários (dict): {'chave': 'valor'}, {'nome': 'João', 'idade': 30}
tuplas (tuple): (1, 2), ('a', 'b'), (1, 'a', True)
conjuntos (set): {1, 2, 3}, {'a', 'b', 'c'}
NoneType (None): None
'''
print(f"O faturamento atual é de {faturamento}") # Função print para exibir algo na tela
print (f"O custo atual é de {custo}") # f-strings para interpolação de variáveis
print (f"O lucro atual é de {faturamento - custo}")