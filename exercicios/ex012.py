# 📌 Calculadora simples com menu interativo

import math

# Função para ler dois números inteiros com validação
def ler_dois_numeros():
    while True:
        try:
            num_01 = int(input('Digite o primeiro número: '))
            num_02 = int(input('Digite o segundo número: '))
            return num_01, num_02
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.')

# Função para ler um único número inteiro com validação
def ler_um_numero():
    while True:
        try:
            num = int(input('Digite um número: '))
            return num
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.')

# Funções para cada operação
def soma():
    num_01, num_02 = ler_dois_numeros()
    print('A soma é:', num_01 + num_02)

def subtracao():
    num_01, num_02 = ler_dois_numeros()
    print('A subtração é:', num_01 - num_02)

def multiplicacao():
    num_01, num_02 = ler_dois_numeros()
    print('A multiplicação é:', num_01 * num_02)

def divisao():
    num_01, num_02 = ler_dois_numeros()
    if num_02 != 0:
        print('A divisão é:', num_01 / num_02)
    else:
        print('⚠ Não é possível dividir por zero!')

def exponenciacao():
    num_01, num_02 = ler_dois_numeros()
    print('A exponenciação é:', num_01 ** num_02)

def fatorial():
    num = ler_um_numero()
    if num < 0:
        print('⚠ Fatorial não definido para números negativos!')
    else:
        print('O fatorial é:', math.factorial(num))

# Loop principal do menu
while True:
    print('\n' + 30 * '-')
    print('📋 Menu Interativo')
    print(30 * '-')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Exponenciação')
    print('6. Fatorial')
    print('7. Sair')
    print(30 * '-')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Entrada inválida! Digite um número de 1 a 7.')
        continue # Volta para o início do loop

    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 5:
        exponenciacao()
    elif opcao == 6:
        fatorial()
    elif opcao == 7:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')
