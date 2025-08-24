import os  # Importa a biblioteca que interage com o sistema operacional

# Lista todos os itens dentro da pasta 'codigos/arquivos'
lista_arquivos = os.listdir("codigos/arquivos")

# Percorre cada item da lista
for nome in lista_arquivos:
    # Verifica se o item é um arquivo .txt
    if nome.endswith(".txt"):
        try:
            # Se o nome contém "22", move para a pasta '22'
            if "22" in nome:
                os.rename(f"codigos/arquivos/{nome}", f"codigos/arquivos/22/{nome}")
                print(f"✅ '{nome}' movido para pasta 22 com sucesso.")
            # Se o nome contém "23", move para a pasta '23'
            elif "23" in nome:
                os.rename(f"codigos/arquivos/{nome}", f"codigos/arquivos/23/{nome}")
                print(f"✅ '{nome}' movido para pasta 23 com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao mover '{nome}': {e}")



