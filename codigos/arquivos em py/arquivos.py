""" # Abre um arquivo, o nome do arquivo esta curto pq ele esta no mesmo local se não seria ex: C://Users/....
arquivo = open("vendas.txt", "r") # w = write, que é modo de escrita, quando vc quer descrever dentro do arquivo, já o r = read, é modo de leitura

#Fazer oq quiser com o arquivo

arquivo.close() # Fechar arquivo """

# Com esse código ele automaticamente fecha o arquivo sem precisar lembrar do .close()
with open ("vendas.txt", "r") as arquivo: 
    #Fazer oq quiser com o arquivo
    infos = arquivo.read() # Ler as informações do arquivo

print(infos) # Tanto faz se é dentro ou fora do withwwwwwwwwwwww