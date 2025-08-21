# Manipulação de Strings e Formatação Numérica em Python

Este arquivo reúne exemplos e explicações sobre manipulação de textos (strings) e formatação de números em Python, úteis para iniciantes e para consulta rápida.



## Manipulação de Strings

- **Alteração de caixa:**
  - `lower()`: converte para minúsculas.
  - `upper()`: converte para maiúsculas.
  - `title()`: primeira letra de cada palavra maiúscula.
  - `capitalize()`: primeira letra da string maiúscula.

- **Remoção de espaços:**
  - `strip()`: remove espaços no início e fim.
  - `lstrip()`: remove espaços à esquerda.
  - `rstrip()`: remove espaços à direita.

- **Busca e extração:**
  - `find(caractere)`: retorna a posição do caractere ou -1 se não encontrar.
  - Slicing: `texto[inicio:fim]` para pegar partes da string.
  - `split(separador)`: divide a string em uma lista.
  - `replace(antigo, novo)`: substitui partes da string.

- **Verificações:**
  - `endswith(sufixo)`: verifica se termina com determinado texto.
  - `startswith(prefixo)`: verifica se começa com determinado texto.
  - `"texto" in string`: verifica se contém determinado texto.

- **Contagem e tamanho:**
  - `len(string)`: retorna o tamanho da string.
  - `count(caractere)`: conta ocorrências de um caractere.



## Exemplos de uso com e-mail

- Extrair o domínio de um e-mail:
  ```python
  posicao = email.find("@")
  servidor = email[posicao:]      # Pega o domínio
  usuario = email[:posicao]       # Pega o usuário
  partes = email.split("@")       # Divide em usuário e domínio
  ```

- Substituir partes do e-mail:
  ```python
  email.replace("gmail", "hotmail")
  ```


## Formatação Numérica

- **Quebra de linha:**  
  Use `\n` para separar informações em linhas diferentes.

- **Separador de milhar e casas decimais:**  
  `f"{valor:,.2f}"` exibe o número com vírgula para milhar e duas casas decimais.

- **Exemplo:**
  ```python
  print(f"Faturamento: R${faturamento:,.2f}")
  ```


## Dicas Extras

- Sempre converta tipos conforme necessário: `str()`, `int()`, `float()`.
- Use f-strings para facilitar a interpolação e formatação de variáveis.
- Métodos de string não alteram o valor original, retornam uma nova string.
- Para manipular textos, combine métodos conforme a necessidade.

