# 💰 Formatação Monetária com `.replace()` no Python

## 🎯 Objetivo

Adaptar a formatação numérica padrão do Python (estilo americano) para o formato brasileiro de moeda, onde:

- O **ponto** é usado como separador de milhar.
- A **vírgula** é usada como separador decimal.

---

## 🔄 Etapas da Substituição com `.replace()`

O Python formata números com vírgula para milhar e ponto para decimal. Para transformar isso no padrão brasileiro, usamos uma sequência de substituições com `.replace()`:

### 1. `replace(",", "X")`
Substitui a vírgula (usada como separador de milhar) por um caractere temporário (`X`).  
Isso evita que a vírgula seja confundida com o separador decimal na próxima etapa.

**Exemplo intermediário:**  
`R$ 100,300.00` → `R$ 100X300.00`

---

### 2. `replace(".", ",")`
Substitui o ponto (usado como separador decimal) por vírgula, conforme o padrão brasileiro.

**Exemplo intermediário:**  
`R$ 100X300.00` → `R$ 100X300,00`

---

### 3. `replace("X", ".")`
Substitui o caractere temporário (`X`) por ponto, restaurando o separador de milhar no formato correto.

**Resultado final:**  
`R$ 100X300,00` → `R$ 100.300,00`

---

## ✅ Resultado

Essa técnica permite exibir valores monetários no padrão brasileiro sem depender de bibliotecas externas, sendo ideal para relatórios simples e exibição em tela.
