import numpy as np
import matplotlib.pyplot as plt

# Criando dados simples
x = np.array([1, 2, 3, 4, 5])
y = x ** 2  # Quadrado de cada valor

# Exibindo os dados
print("x:", x)
print("y:", y)

# Criando o gráfico de linha com pontos marcados
plt.plot(x, y, marker='o')  # Plota y = x² com marcadores circulares
plt.title('Gráfico de y = x²')  # Título do gráfico
plt.xlabel('x')  # Rótulo do eixo x
plt.ylabel('y')  # Rótulo do eixo y
plt.grid(True)  # Adiciona uma grade ao fundo
plt.show()  # Exibe o gráfico na tela
""" # Salvando o gráfico como uma imagem
plt.savefig('grafico_y_x2.png')  # Salva o gráfico como um arquivo PNG
plt.close()  # Fecha a figura atual """
