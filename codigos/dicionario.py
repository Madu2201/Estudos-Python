""" o Dicionário garante que qualquer informação é única(Chave), 
pois caso tente adcionar uma igual ele edita a existente """


""" # Usando dicionário para mapear produtos aos preços
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
    print("Produto não encontrado!") """


# Criando um dicionário inicial
produto = {
    "nome": "Celular",
    "preco": 1500,
    "estoque": 10
}

# .keys() → retorna todas as chaves
print("🔑 Chaves:", produto.keys())

# .values() → retorna todos os valores
print("📦 Valores:", produto.values())

# .items() → retorna pares (chave, valor)
print("🧾 Itens:", produto.items())

# .get() → acessa valor de forma segura
print("📍 Preço:", produto.get("preco"))  # retorna 1500
print("📍 Cor:", produto.get("cor"))      # retorna None (não dá erro)

# .update() → atualiza ou adiciona novos pares
produto.update({"preco": 1600, "cor": "preto"})
print("🔄 Atualizado:", produto)

# .setdefault() → retorna valor da chave ou insere se não existir
produto.setdefault("garantia", "12 meses")
print("🛡️ Com garantia:", produto)

# .pop() → remove uma chave específica e retorna seu valor
estoque_removido = produto.pop("estoque")
print("❌ Estoque removido:", estoque_removido)
print("📦 Após remoção:", produto)

# .popitem() → remove o último item inserido
ultimo = produto.popitem()
print("🧹 Último item removido:", ultimo)
print("📦 Após popitem:", produto)

# Verificando se uma chave existe com 'in'
if "nome" in produto:
    print("✅ A chave 'nome' existe!")

# Usando del para remover uma chave
del produto["preco"]
print("🗑️ Após deletar 'preco':", produto)

# .clear() → remove todos os itens
produto.clear()
print("🚫 Dicionário vazio:", produto)

# len() → número de itens no dicionário
novo_dict = {"a": 1, "b": 2, "c": 3}
print("📏 Tamanho do novo_dict:", len(novo_dict))
