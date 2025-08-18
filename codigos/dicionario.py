# Usando dicionário para mapear produtos aos preços
produtos = {
    "celular": 1500,
    "camera": 1000,
    "fone de ouvido": 800,
    "monitor": 2000
}

# Entrada do usuário
consulta_usuario = input("Digite o nome do produto para consulta: ").lower()

# Verificação e resposta
if consulta_usuario in produtos:
    print(f"O preço desse produto é R$ {produtos[consulta_usuario]}")
else:
    print("Produto não encontrado!")