faturamento = 1000
custo = 700

lucro = faturamento - custo

'''
print (f"Faturamento: R${faturamento:}, Custo: {custo}, Lucro: {lucro}") # Formatação de string com f-strings
print ("Faturamento:" + str(faturamento)) # Concatenação de string com conversão de tipo
'''

email = "EMAIL_falso@gmail.com"

''' Manipulação de strings em Python
print(email.lower())  # Converte o email para minúsculas
print(email.upper())  # Converte o email para maiúsculas
print(email.title())  # Converte o email para título (primeira letra maiúscula de cada palavra)
print(email.capitalize())  # Converte o email para capitalizado (primeira letra maiúscula da string)
print(email.strip())  # Remove espaços em branco no início e no final do email
print(email.lstrip())  # Remove espaços em branco no início do email
print(email.rstrip())  # Remove espaços em branco no final do email
'''

'''
Encontra a posição do caractere '@' no email, 
serve para encontrar qualquer caractere, vai 
retornar -1 se não encontrar e a posição se encontrar
que no é o caso é 11. Cada caractere conta como uma posição,
iniciando do 0.

print(email.find("@")) 
print(email[11])  # Acessa o caractere na posição 11 do email

# Acessa o pedaço do email a partir da posição 11
posicao = email.find("@")
servidor = email[posicao:] # Acessa o pedaço do email a partir da posição 11
print(servidor)  # Imprime o pedaço do email a partir da posição 11
print(email[:posicao])  # Imprime o pedaço do email do início até a posição do '@'

# Pode colocar números após os dois pontos para limitar o tamanho do pedaço, os : significa até
print(email[posicao + 1:])  # Imprime o pedaço do email a partir da posição do '@' + 1

# Verifica se o email termina com '.com', retorna True ou False
print(email.endswith(".com"))  # Verifica se o email termina com '.com'

# Verifica se o email começa com 'EMAIL_', retorna True ou False
print(email.startswith("EMAIL_"))  # Verifica se o email começa com 'EMAIL_'

# Verifica se o email contém 'gmail', retorna True ou False
print("gmail" in email)  # Verifica se o email contém 'gmail' 

# Divide o email em duas partes: antes e depois do '@'. O método split() divide a string em uma lista
print(email.split("@"))  # Divide o email em duas partes: antes e depois do '@'
print(email.split("@")[0])  # Acessa a parte antes do '@'
print(email.split("@")[1])  # Acessa a parte depois do '@'

# O método replace() substitui uma parte da string por outra
print(email.replace("EMAIL_", "Madu_"))  # Substitui 'EMAIL_' por 'Madu_' no email
print(email.replace("gmail", "hotmail"))  # Substitui 'gmail' por 'hotmail' no email
print(email.replace("EMAIL_", "Madu_").replace("gmail", "hotmail"))  # Substitui 'EMAIL_' por 'Madu_' e 'gmail' por 'hotmail' no email

print(len(email))  # Imprime o tamanho do email
print(email.count("a"))  # Conta quantas vezes o caractere 'a' aparece

'''

# Formatação numerica em Python
print (f"Faturamento: R${faturamento}\n Custo: {custo}\n Lucro: {lucro}") # \n quebra de linha
print(f"Faturamento: R${faturamento:,.2f}, Custo: {custo:,.2f}, Lucro: {lucro:,.2f}")  # Formata o faturamento, custo e lucro com vírgula como separador de milhar e duas casas decimais float

