# 1° Pegar o primeiro nome do usuário
# 2° Pegar servidor e domínio do e-mail
# 3° Construa uma mensagem : Enviamos um link de confirmação para o e-mail j***@gmail.com

'''
Só usar o input() para pegar o nome do usuário, o input() já converte o valor para string, então 
converter sempre que for utilizar com números.
Não precisa usar o print() para exibir o valor do input, pois o input já exibe o valor digitado
'''
# Solicita o nome e o e-mail do usuário
nome = input("Digite o seu nome:")
email = input("Digite o seu e-mail:")

# Função para pegar o primeiro nome do usuário
def primeiro_nome(nome):
    # Verifica se o nome está vazio
    if nome == "":
        return "Nome não informado"
    elif " " in nome:
        # Se houver espaço, pega o primeiro nome
        return nome.split()[0]
    else:
        # Se não houver espaço, retorna o nome completo
        return nome


print(f"Olá, {primeiro_nome(nome)}!")  # Imprime o primeiro nome do usuário

# Exibir a lista do método split()
# print(nome.split())  # Imprime a lista de nomes divididos

# Função para descobrir o servidor do e-mail
def Dominioservidor_email(email):
    posicao = email.find("@")  # Encontra a posição do '@'

    if posicao != -1:  # Verifica se o '@' foi encontrado
        usuario, servidor = email.split("@")
        return usuario, servidor
    else:
        return "Usuário inválido", "E-mail inválido"


usuario, servidor = Dominioservidor_email(email)
print(f"O usuário do e-mail é: {usuario}")
print(f"O servidor do e-mail é: {servidor}")

# Função para mascarar o e-mail
def mascara_email(email):
    if "@" in email:
        usuario, dominio = email.split("@") # Divide o e-mail em usuário e domínio
        if len(usuario) > 3: # Se o usuário tiver mais de 3 caracteres
            # Mascarar os caracteres do usuário, mantendo os 3 primeiros
            usuario_mascara = usuario[:3] + "***"
        else: # Se o usuário tiver 3 ou menos caracteres
            # Manter o usuário completo, mas mascarar os últimos 3 caracteres
            usuario_mascara = usuario + "***"
        return f"{usuario_mascara}@{dominio}" # Retorna o e-mail mascarado
    else:
        return "E-mail inválido"
    
print(f"Olá, Usuário {primeiro_nome(nome)} cadastrado com sucesso! Enviamos um link de confirmação para o e-mail {mascara_email(email)}")