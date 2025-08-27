# Matplotlib

Matplotlib é uma biblioteca poderosa para criação de gráficos e visualizações em Python. Ela permite gerar gráficos estáticos, animados e interativos, sendo amplamente utilizada em ciência de dados, engenharia, estatística e áreas afins.

## Principais Recursos

- **Gráficos de Linha:** Ideal para mostrar tendências ao longo do tempo.
- **Gráficos de Barras:** Úteis para comparar valores entre categorias.
- **Gráficos de Dispersão:** Visualizam a relação entre duas variáveis.
- **Histogramas:** Mostram a distribuição de dados.
- **Gráficos de Pizza, Área, Boxplot, e outros:** Diversas opções para diferentes necessidades.
- **Personalização:** Controle total sobre cores, estilos, tamanhos, legendas, títulos, e eixos.
- **Subplots:** Criação de múltiplos gráficos em uma mesma figura.
- **Anotações:** Adição de textos, setas e destaques nos gráficos.
- **Exportação:** Salve gráficos em diversos formatos (PNG, PDF, SVG, etc.).

## Exemplo Básico

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o', color='blue', linestyle='--', label='Dados')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Exemplo de Gráfico de Linha')
plt.legend()
plt.grid(True)
plt.show()
```

---

# Comandos e Funções Principais do Matplotlib


## Criação de Gráficos

| Comando                  | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| `plt.plot(x, y, ...)`    | Cria gráfico de linha.                                                    |
| `plt.bar(x, y, ...)`     | Cria gráfico de barras.                                                   |
| `plt.scatter(x, y, ...)` | Cria gráfico de dispersão (pontos).                                       |
| `plt.hist(x, ...)`       | Cria histograma (distribuição de dados).                                  |
| `plt.pie(x, ...)`        | Cria gráfico de pizza.                                                    |
| `plt.boxplot(x, ...)`    | Cria boxplot (distribuição e outliers).                                   |
| `plt.fill_between(x, y1, y2)` | Cria gráfico de área entre duas curvas.                              |

---

## Personalização

| Comando                      | Descrição                                              |
|------------------------------|--------------------------------------------------------|
| `plt.xlabel('texto')`        | Define o nome do eixo X.                               |
| `plt.ylabel('texto')`        | Define o nome do eixo Y.                               |
| `plt.title('texto')`         | Define o título do gráfico.                            |
| `plt.legend()`               | Exibe a legenda do gráfico.                            |
| `plt.grid(True)`             | Adiciona grade ao gráfico.                             |
| `plt.xlim(inicio, fim)`      | Define limites do eixo X.                              |
| `plt.ylim(inicio, fim)`      | Define limites do eixo Y.                              |
| `plt.xticks([...])`          | Define os valores dos ticks do eixo X.                 |
| `plt.yticks([...])`          | Define os valores dos ticks do eixo Y.                 |

---

## Subplots e Figuras

| Comando                                 | Descrição                                              |
|------------------------------------------|--------------------------------------------------------|
| `plt.figure(figsize=(w, h))`             | Cria uma nova figura com tamanho definido.             |
| `plt.subplots(nrows, ncols)`             | Cria múltiplos gráficos em uma mesma figura.           |
| `fig, axs = plt.subplots(...)`           | Retorna figura e eixos para manipulação avançada.      |

---

## Anotações e Destaques

| Comando                        | Descrição                                              |
|--------------------------------|--------------------------------------------------------|
| `plt.annotate('texto', xy=(x, y))` | Adiciona texto em uma posição específica.           |
| `plt.text(x, y, 'texto')`           | Adiciona texto livre no gráfico.                    |
| `plt.axhline(y)`                     | Adiciona linha horizontal.                          |
| `plt.axvline(x)`                     | Adiciona linha vertical.                            |

---

## Exibição e Salvamento

| Comando                      | Descrição                                              |
|------------------------------|--------------------------------------------------------|
| `plt.show()`                 | Exibe o gráfico na tela.                               |
| `plt.savefig('arquivo.png')` | Salva o gráfico em arquivo (PNG, PDF, SVG, etc.).      |

---

## Parâmetros Comuns

- **`color`**: Define a cor (`'red'`, `'blue'`, `'#123456'`, etc.).
- **`marker`**: Define o marcador dos pontos (`'o'`, `'s'`, `'^'`, etc.).
- **`linestyle`**: Define o estilo da linha (`'-'`, `'--'`, `':'`, `'-.'`).
- **`label`**: Define o nome para legenda.

---

## Documentação

Consulte a documentação oficial para exemplos detalhados e tutoriais:  
[https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)