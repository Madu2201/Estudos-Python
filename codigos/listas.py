vendas = [100, 50, 130] # Lista com números
#produtos = ["iphone, ipad, airpod", "tablet, celular"] # Lista com 2 itens

print(vendas[-1]) # Quando passa um índice negativo ele pega da direita para esquerda, ou seja, o último elemento
print(vendas[0]) # Primeiro elemento da lista

total_vendas = sum(vendas) # Soma os valores da lista vendas
print(total_vendas)

quantidades = len(vendas) # Mostra o tamanho da lista vendas, contando os itens
print(quantidades)

valor_max = max(vendas) # Pega o maior valor da lista
valor_min = min(vendas) # Pega o menor valor da lista
print(valor_max , valor_min)

posicao = vendas.index(130) # Vai descobrir em qual posição da sua lista está o 130
print(posicao) # Índice 2

print(vendas[:2]) # Pega os valores antes do índice 2
print(vendas[1:]) # Pega os valores depois do índice 1


produtos = ["iphone", "ipad", "airpod"] # Lista com 3 itens

print("iphone" in produtos) # in é um operador que vai verificar se está contido, ou seja, se produtos tem "iphone" e vai retornar true ou false

produto_usuario = input("Digite o nome de um produto: ")
print(produto_usuario in produtos) # Vai verificar se o produto digitado pelo usuário está na lista produtos

# Editar informações
precos = [4000, 3000, 2000]
precos[0] = 4500 # Editando o valor da lista de índice 0 que é 4000 para 4500
print(precos)
precos[0] *= 1.1 # Tem como fazer operações
print(precos)

# Adcionando um item
produtos.append("macbook") 

# Removendo um item
produtos.remove("macbook") # Removendo pelo valor do item
precos.pop(-1) # Remove pelo índice
print(produtos)
print(precos)

# Inserir um valor
produtos.insert(1 , "celular") # Adciona um item, primeiro indice depois o valor
print(produtos)

# Contar valores
print(produtos.count("airpod")) # Quantidade de vezes que o item aparece

# Ordenar lista - Tanto para number quanto string 
precos.sort() # Crescente
print(precos)

precos.reverse() # Decrescente
print(precos)
