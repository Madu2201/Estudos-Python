# 📄 Explicação do Código: Cálculo de Impostos

Este script define uma função para calcular três tipos de impostos sobre um valor fixo, e exibe os resultados de forma organizada.

---

## 🧮 Função `calcular_imposto2`

A função recebe um valor (`preço`) e calcula os seguintes impostos:

- **IR (Imposto de Renda)**: 27,5% do valor
- **CSLL (Contribuição Social sobre o Lucro Líquido)**: 3,5% do valor
- **ISS (Imposto Sobre Serviços)**: 5% do valor

Essas alíquotas são definidas como **valores padrão**, mas podem ser alteradas ao chamar a função.

A função retorna os três valores como uma **tupla**, que é uma estrutura imutável em Python, ou seja, não pode ser alterada.

---

## 🔁 Chamada da Função

A função é chamada com o valor `1000`, e os três impostos são atribuídos diretamente às variáveis `ir`, `csll` e `iss` usando **unpacking**, que atribui cada valor da tupla a uma variável.

---

## 📤 Exibição dos Resultados

Os valores dos impostos são exibidos com o comando `print`, usando `sep="\n"` para que cada valor apareça em uma linha separada, esse `sep="\n"` é um parâmetro que pode ser usado no `print`.

---

## 🧠 Observações

- A tupla retornada permite agrupar múltiplos valores de forma compacta e imutável.
- O uso de `sep="\n"` melhora a legibilidade da saída.
- O código está preparado para ser reutilizado com outros valores e alíquotas, se necessário.

---

## ✅ Resultado Esperado

Para o valor de `1000`, os impostos calculados são:

- IR: 275.0
- CSLL: 35.0
- ISS: 50.0

Cada valor será exibido em uma linha separada no terminal.

