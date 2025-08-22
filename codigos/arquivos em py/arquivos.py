""" # ---------------------- MODO MANUAL ----------------------
# Abre o arquivo 'vendas.txt' no modo de leitura ('r')
# Nesse modo, é necessário lembrar de fechar o arquivo manualmente
arquivo = open("vendas.txt", "r")  # 'w' = escrita, 'r' = leitura

# Lê o conteúdo do arquivo
# Aqui você pode fazer qualquer operação com o conteúdo
conteudo = arquivo.read()

# Fecha o arquivo manualmente após o uso
arquivo.close()

# Exibe o conteúdo lido
print(conteudo) """


# ---------------------- MODO AUTOMÁTICO COM 'with' ----------------------
# Abre o arquivo usando o caminho absoluto, no modo de leitura
# O bloco 'with' garante que o arquivo será fechado automaticamente ao final
with open("c:/Users/dudac/OneDrive/Área de Trabalho/Madu/Programação/Visual Studio Code/Estudos-Python/codigos/arquivos em py/vendas.txt", "r") as arquivo:
    # Lê todas as linhas do arquivo e retorna uma lista
    # Cada item da lista é uma linha do arquivo, como: "Andre, 300\n"
    infos = arquivo.readlines() # A variável infos é uma lista de strings

# Inicializa a variável que vai acumular o total de vendas
vendas_tot = 0

# Percorre cada linha da lista 'infos'
for item in infos:
    # Remove quebras de linha e espaços extras
    item = item.replace("\n", "")
    item = item.replace(" ", "")

    # Separa os dados da linha usando vírgula como delimitador
    resultado = item.split(",")  # Exemplo: ["Andre", "300"]

    # Pega o segundo elemento (valor da venda)
    valor = resultado[1]

    # Converte o valor para float
    valor = float(valor)

    # Soma ao total de vendas
    vendas_tot += valor

# Exibe o total de vendas
print(vendas_tot)

