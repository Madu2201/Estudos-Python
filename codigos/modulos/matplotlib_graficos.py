import numpy as np
import matplotlib.pyplot as plt

# ================================
# 📊 Gráfico de Barras
# ================================

# Dados categóricos e seus respectivos valores
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Cria um gráfico de barras verticais
plt.bar(categorias, valores, color='skyblue')  # cor personalizada
plt.title('Gráfico de Barras')                 # título do gráfico
plt.xlabel('Categorias')                       # rótulo do eixo x
plt.ylabel('Valores')                          # rótulo do eixo y
plt.show()                                     # exibe o gráfico

# ================================
# 🥧 Gráfico de Pizza
# ================================

# Rótulos e tamanhos das fatias
labels = ['Maçã', 'Banana', 'Laranja', 'Uva']
tamanhos = [30, 25, 25, 20]

# Cria um gráfico de pizza com porcentagens
plt.pie(tamanhos, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Frutas')  # título do gráfico
plt.axis('equal')                    # mantém o círculo proporcional
plt.show()

# ================================
# 🔵 Gráfico de Dispersão
# ================================

# Dados de coordenadas x e y
x = [1, 2, 3, 4, 5]
y = [5, 4, 6, 7, 5]

# Cria um gráfico de dispersão (pontos)
plt.scatter(x, y, color='purple')     # cor dos pontos
plt.title('Gráfico de Dispersão')     # título do gráfico
plt.xlabel('x')                       # rótulo do eixo x
plt.ylabel('y')                       # rótulo do eixo y
plt.grid(True)                        # adiciona grade
plt.show()

# ================================
# 📈 Histograma
# ================================

# Gera 1000 valores com distribuição normal (média=0, desvio=1)
dados = np.random.normal(0, 1, 1000)

# Cria um histograma com 30 faixas (bins)
plt.hist(dados, bins=30, color='green', edgecolor='black')  # borda preta nas barras
plt.title('Histograma de Dados')     # título do gráfico
plt.xlabel('Valor')                  # rótulo do eixo x
plt.ylabel('Frequência')             # rótulo do eixo y
plt.show()



