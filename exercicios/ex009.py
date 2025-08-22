# Inicializa uma lista vazia chamada 'tabela' que vai armazenar as linhas da matriz
tabela = []

# Inicializa a variável 'c' com o valor 1, que será usado para preencher a matriz sequencialmente
c = 1

# Loop externo para criar 3 linhas (índice i de 0 a 2)
for i in range(3):
    # Cria uma lista vazia chamada 'linha' para armazenar os elementos da linha atual
    linha = []

    # Loop interno para criar 3 colunas (índice j de 0 a 2)
    for j in range(3):
        # Adiciona o valor atual de 'c' à linha
        linha.append(c)

        # Incrementa 'c' para o próximo número
        c += 1

    # Adiciona a linha completa à tabela
    tabela.append(linha)

# Exibe a matriz final
print(tabela)

# Saída esperada:
# [[1, 2, 3], 
#  [4, 5, 6], 
#  [7, 8, 9]]
