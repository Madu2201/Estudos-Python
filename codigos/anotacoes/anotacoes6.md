# 📚 Conceitos de Python: `sep` e Unpacking

Este documento explica dois conceitos fundamentais usados com frequência em Python: o parâmetro `sep` na função `print()` e o processo de **unpacking** de coleções.

[Ver código completo](/codigos/tuplas.py)


---

## 🖨️ `sep` no `print()`

O parâmetro `sep` (abreviação de *separator*) é usado para definir o separador entre os valores exibidos pela função `print()`.

### ✅ Características:
- É um argumento opcional da função `print()`.
- Permite personalizar como os valores são separados na saída.

### 🔹 Exemplos:
- `sep=" "` → separa os valores com espaço (comportamento padrão).
- `sep=","` → separa os valores com vírgula.
- `sep="\n"` → imprime cada valor em uma nova linha.

### 🔹 Utilidade:
Ajuda a formatar a saída do programa de forma mais legível e organizada.

---

## 📦 Unpacking

**Unpacking** é o processo de extrair os elementos de uma coleção (como tupla ou lista) e atribuí-los diretamente a variáveis individuais.

### ✅ Características:
- Funciona com tuplas, listas e outros iteráveis.
- Atribui os valores na ordem em que aparecem.

### 🔹 Exemplo:
```python
a, b, c = (10, 20, 30)

**Nesse exemplo:**

`a recebe 10`

`b recebe 20`

`c recebe 30`
```

---

## 🧠 Conclusão

- Use sep para controlar a formatação da saída com print().

- Use unpacking para extrair valores de coleções de forma clara e eficiente.

- Esses dois recursos tornam o código mais legível, organizado e profissional.