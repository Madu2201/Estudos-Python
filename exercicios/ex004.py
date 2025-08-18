# Lista de preços dos produtos
precos = [1500, 1000, 800, 2000]

# Lista de nomes dos produtos correspondentes aos preços
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# Solicita ao usuário que digite o nome de um produto
# Converte o texto digitado para letras minúsculas para evitar erros de capitalização
consulta_usuario = input("Digite o nome do produto para consulta: ").lower()

# Verifica se o produto digitado está na lista de produtos
if consulta_usuario in produtos:
    # Encontra a posição (índice) do produto na lista
    posicao = produtos.index(consulta_usuario)
    
    # Usa a mesma posição para acessar o preço correspondente na lista de preços
    preco = precos[posicao]
    
    # Exibe o nome do produto e o preço formatado com duas casas decimais
    print(f"Produto: {consulta_usuario}, Preço: {preco:.2f}")
else:
    # Se o produto não estiver na lista, exibe uma mensagem de erro
    print("Produto não encontrado, tente novamente")



""" # Lista de preços dos produtos
precos = [1500, 1000, 800, 2000]

# Lista de nomes dos produtos correspondentes aos preços
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# Solicita ao usuário que digite o nome de um produto e converte para minúsculas
consulta_usuario = input("Digite o nome do produto para consulta: ").lower()

# Verifica se o produto digitado corresponde ao primeiro item da lista
if consulta_usuario == produtos[0]:
    print(f"O preço desse produto é {precos[0]}")

# Verifica se corresponde ao segundo item
elif consulta_usuario == produtos[1]:
    print(f"O preço desse produto é {precos[1]}")

# Verifica se corresponde ao terceiro item
elif consulta_usuario == produtos[2]:
    print(f"O preço desse produto é {precos[2]}")

# Verifica se corresponde ao quarto item
elif consulta_usuario == produtos[3]:
    print(f"O preço desse produto é {precos[3]}")

# Se não corresponder a nenhum item da lista, exibe mensagem de erro
else:
    print("Produto não encontrado!")
 """


""" # Usando função para o mesmo exercício
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

# Função que consulta o preço de um produto
def consultar_preco(nome_produto):
    nome_produto = nome_produto.lower()
    
    # Verifica se o produto está na lista
    if nome_produto in produtos:
        indice = produtos.index(nome_produto)
        print(f"O preço do produto '{produtos[indice]}' é R$ {precos[indice]}")
    else:
        print("Produto não encontrado!")


# Execução principal
consulta_usuario = input("Digite o nome do produto para consulta: ")
consultar_preco(consulta_usuario) """

