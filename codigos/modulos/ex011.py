# Loop externo para gerar as tabuadas de 1 a 10
for numerador in range(10):
    # Imprime o cabeçalho da tabuada atual
    print(f"Tabuada do número {numerador + 1}")
    
    # Loop interno para multiplicar o número atual por valores de 1 a 10
    for multiplicador in range(10):
        # Calcula e imprime o resultado da multiplicação
        print(f"{numerador + 1} x {multiplicador + 1} = {(numerador + 1) * (multiplicador + 1)}")

