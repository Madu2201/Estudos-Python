## Operadores Matemáticos em Python

- **Adição (`+`)**: Soma valores.
- **Subtração (`-`)**: Subtrai valores.
- **Multiplicação (`*`)**: Multiplica valores.
- **Divisão (`/`)**: Divide valores (resultado float).
- **Divisão inteira (`//`)**: Divide e retorna o inteiro.
- **Módulo (`%`)**: Retorna o resto da divisão.
- **Exponenciação (`**`)**: Eleva à potência.

---

## Ordem de Precedência

A ordem de execução dos operadores segue:
1. Parênteses `()`
2. Exponenciação `**`
3. Multiplicação, Divisão, Módulo `*`, `/`, `//`, `%`
4. Adição e Subtração `+`, `-`

Use parênteses para garantir o resultado desejado.

---

## Formatação de Números

- **Arredondamento:**  
  `round(valor)` para inteiro mais próximo,  
  `round(valor, n)` para n casas decimais.
- **Porcentagem:**  
  `f"{valor:.2%}"` exibe como porcentagem com duas casas decimais.
- **Separador de milhar:**  
  Use `_` para facilitar leitura de números grandes, ex: `1_000_000`.

---

## Conversão de Tipos Numéricos

- Para inteiro: `int(valor)`
- Para decimal: `float(valor)`
- Para texto: `str(valor)`

---

## Dicas Gerais

- Sempre converta tipos conforme necessário para cálculos ou exibição.
- Use formatação nas f-strings para controlar casas decimais e símbolos.
- O operador `%` é útil para cálculos de tempo e divisões com resto.
- O Python trata inteiros (`int`) e decimais (`float`) de forma diferente em