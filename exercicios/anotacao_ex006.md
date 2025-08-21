# 💼 Cálculo de Bônus dos Vendedores

Este documento explica como funciona o cálculo de bônus para vendedores com base em suas vendas semanais.

---

## 📊 Estrutura dos Dados

Os dados de vendas estão organizados em um **dicionário**, onde:

- Cada **chave** representa o nome de um vendedor.
- Cada **valor** é uma lista contendo os valores das vendas realizadas por esse vendedor.

---

## 💰 Regras para o Cálculo do Bônus

Cada venda gera dois tipos de bônus:

- **Bônus fixo**: R$2 por venda realizada.
- **Bônus variável**: 1% do valor total das vendas.

### 🧮 Fórmula do Bônus Total

Para cada vendedor, o bônus total é calculado da seguinte forma:

`Bônus Total = (Quantidade de Vendas × R$2) + (1% do Valor Total das Vendas)`


---

## 🔁 Lógica do Programa

1. Uma função é definida para calcular o bônus com base na lista de vendas de cada vendedor.
2. O programa percorre o dicionário de vendas usando um laço de repetição.
3. Para cada vendedor:
   - Calcula o bônus total usando a função.
   - Exibe o nome do vendedor e o valor do bônus formatado.
   - Soma o bônus ao total geral.
4. Ao final, imprime o valor total de bônus pago pela empresa.

---

## 🧠 Observações Adicionais

- O programa utiliza o método `.items()` para acessar pares de chave e valor no dicionário.
- Há um trecho comentado que demonstra como fazer o "desempacotamento" das tuplas geradas pelo `.items()` para acessar diretamente o nome do vendedor e sua lista de vendas.

---

## ✅ Resultado Esperado

- Exibição do bônus individual de cada vendedor.
- Exibição do valor total de bônus pago pela empresa.

