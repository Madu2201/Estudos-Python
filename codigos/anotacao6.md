# 💰 Formatação Monetária com `.replace()` no Python

## 🎯 Objetivo

Adaptar a formatação numérica padrão do Python (estilo americano) para o formato brasileiro de moeda, onde:

- O **ponto** é usado como separador de milhar.
- A **vírgula** é usada como separador decimal.

---

## 🔄 Etapas da Substituição

1. **Troca da vírgula por um caractere temporário (`X`)**  
   Isso evita conflitos ao substituir o ponto por vírgula posteriormente.

2. **Troca do ponto por vírgula**  
   Altera o separador decimal para o padrão brasileiro.

3. **Troca do caractere temporário (`X`) por ponto**  
   Restaura o separador de milhar no formato correto.

---

## 📌 Exemplo de Transformação

Formato original (americano):  
`R$ 100,300.00`

Após as substituições:  
`R$ 100.300,00`

---

## ✅ Resultado

Essa técnica permite exibir valores monetários no padrão brasileiro sem depender de bibliotecas externas, sendo ideal para relatórios simples e exibição em tela.
