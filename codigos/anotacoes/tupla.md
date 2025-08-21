# 📦 O Que é uma Tupla em Python?

Uma **tupla** é uma estrutura de dados em Python usada para armazenar múltiplos valores em uma única variável. Ela é **imutável**, ou seja, seus elementos não podem ser alterados depois de criada.

[Ver código completo](/codigos/tuplas.py)

---

## 🔑 Características Principais

- **Sintaxe**: definida com parênteses `()`
- **Imutável**: não permite modificações após a criação
- **Ordenada**: os elementos mantêm a ordem de inserção
- **Permite duplicatas**: pode conter valores repetidos
- **Acessível por índice**: como listas, os elementos podem ser acessados por posição

---

## 🧠 Quando Usar Tuplas?

- Quando os dados não devem ser alterados
- Para retornar múltiplos valores de uma função
- Para representar registros fixos (ex: coordenadas, datas, etc.)

---

## 📤 Exemplo de Uso

Imagine uma função que retorna três valores de imposto. Ela pode usar uma tupla para agrupar os resultados:

```python
return imposto_ir, imposto_csll, imposto_iss
