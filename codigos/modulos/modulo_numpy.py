import numpy as np

# Criando arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Operações matemáticas
soma = a + b 
subtracao = b - a
multiplicacao = a * b
divisao = b / a

# Estatísticas
media = np.mean(a)
mediana = np.median(b)
desvio = np.std(b)

# Operações com matriz
matriz = np.array([[1, 2], [3, 4]])
transposta = matriz.T
determinante = np.linalg.det(matriz)

print(f"Array A:{a}\n")
print(f"Array B:{b}\n")
print(f"Soma:{soma}\n")
print(f"Subtração:{subtracao}\n")
print(f"Multiplicação:{multiplicacao}\n")
print(f"Divisão:{divisao}\n")
print(f"Média de A:{media}\n")
print(f"Mediana de B:{mediana}\n")
print(f"Desvio padrão de B:{desvio}\n")
print(f"Matriz:\n{matriz}\n")
print(f"Transposta:\n{transposta}\n")
print(f"Determinante da matriz:{determinante}\n")

