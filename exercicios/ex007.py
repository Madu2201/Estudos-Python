# Lista inicial de clientes na fila de atendimento
listaClientes = ["José", "Pedro", "Rafael", "Amanda"]

# Loop infinito para manter o programa em execução até que seja interrompido manualmente
while True:
    # Exibe o menu de opções
    print("------------------------")
    print("1 - Novo Cliente")       # Opção para adicionar um novo cliente à fila
    print("2 - Atender Cliente")   # Opção para iniciar o atendimento de um cliente

    # Solicita ao usuário que escolha uma das opções
    acao = int(input("Qual opção deseja escolher? "))

    # Se a opção escolhida for 1, adiciona um novo cliente à fila
    if acao == 1:
        # Mostra a fila atual de clientes
        print(f"Fila de atendimento: {listaClientes}")

        # Solicita o nome do novo cliente
        novoCliente = input("Novo Cliente ")

        # Adiciona o novo cliente ao final da fila
        listaClientes.append(novoCliente)

        # Mostra a fila atualizada
        print(f"Fila de atendimento: {listaClientes}")

        # Confirma que o cliente foi cadastrado com sucesso
        print("Cliente cadastrado com sucesso!")

    # Se a opção escolhida for 2, inicia o atendimento do primeiro cliente da fila
    if acao == 2:
        # Percorre a lista de clientes (mas só atende o primeiro por causa do break)
        for cliente in listaClientes:
            while True:
                # Inicia o atendimento do cliente atual
                print(f"Atendendo {cliente}")

                # Solicita ao usuário que digite 0 para encerrar o atendimento
                flag = int(input("Digite 0 para encerrar atendimento "))

                # Mostra a fila atual de atendimento
                print(f"Fila de atendimento: {listaClientes}")

                # Se o usuário digitar 0, encerra o atendimento
                if flag == 0:
                    # Remove o primeiro cliente da fila
                    del(listaClientes[0])

                    # Mostra a nova fila após o atendimento
                    print(f"Nova fila de atendimento: {listaClientes}")

                    # Sai do loop interno de atendimento
                    break

            # Sai do loop externo após atender o primeiro cliente
            break
