# 📘 Explicação do Código de Análise de Vendas

Este documento detalha o funcionamento de um código Python que analisa e simula o desempenho de vendas mensais de uma empresa nos anos de 2022 e 2023.

[Ver código completo](exercicios/ex005.py)

---

## 🗂️ Estrutura dos Dados

Os dados de vendas estão organizados em dois dicionários:
- `vendas_22`: contém os valores mensais de 2022.
- `vendas_23`: contém os valores mensais de 2023.

Cada chave representa um mês (`"jan"`, `"fev"`, etc.) e o valor associado representa o faturamento daquele mês.

---

## 1️⃣ Cálculo da Variação Percentual

### 🎯 Objetivo:
Comparar o desempenho de cada mês de 2023 com o mesmo mês de 2022, mostrando a variação percentual.

### 🧠 Lógica:
- Itera sobre os meses de 2023.
- Para cada mês:
  - Recupera os valores de 2022 e 2023.
  - Calcula a variação percentual com a fórmula:


` var_percentual = valor_23 / valor_22 - 1`


- Exibe o resultado formatado como porcentagem com uma casa decimal.

### 📌 Exemplo de saída:

`Variação do jan:` 13.3% 

`Variação do fev:` -3.2%

---

## 2️⃣ Simulação de Faturamento Sem Quedas

### 🎯 Objetivo:
Simular o faturamento total de 2023 caso a empresa tivesse **pelo menos igualado** os valores de 2022 nos meses em que houve queda.

### 🧠 Lógica:
- Inicializa uma variável para acumular o faturamento simulado.
- Para cada mês:
  - Compara os valores de 2023 com 2022.
  - Se 2023 teve queda, soma o valor de 2022 (simulando empate).
  - Se 2023 teve crescimento ou empate, soma o valor real de 2023.
- Exibe a variação percentual de cada mês e o faturamento total simulado.

### 📌 Exemplo de saída:

`Variação do fev:` -3.2% 

`Variação do mai:` -1.8% 

`Faturamento total simulado:` R$ 100.300,00

---

## ✅ Conclusão

Este código permite:
- Avaliar o desempenho mês a mês.
- Identificar meses com queda nas vendas.
- Estimar o impacto financeiro de manter o faturamento estável nos meses de baixa.

