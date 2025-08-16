## Anotações sobre o código `codigo.py`

### Sobre os comentários

- Comentários em Python são feitos com `#` para uma linha ou com aspas triplas `'''` para múltiplas linhas.
- Servem para explicar o funcionamento do código, facilitar o entendimento e registrar observações importantes.

### Explicações dos comentários do código

- `taxa_imposto = 0.1`  
  **Comentário:** 10% de imposto, escreve-se de forma decimal.

- Bloco de tipos de dados:
  ```
  números inteiros(int): 1, 2, 3, -10, -50
  números decimais (float): 1.5, 0.75, -10.99
  strings (str): "Olá", 'Mundo', '1234'
  booleanos (bool): True, False
  listas (list): [1, 2, 3], ['a', 'b', 'c'], [1, 'a', True]
  dicionários (dict): {'chave': 'valor'}, {'nome': 'João', 'idade': 30}
  tuplas (tuple): (1, 2), ('a', 'b'), (1, 'a', True)
  conjuntos (set): {1, 2, 3}, {'a', 'b', 'c'}
  NoneType (None): None
  ```
  **Comentário:** Explicação dos principais tipos de dados em Python.

- `print(f"O faturamento atual é de {faturamento}")`  
  **Comentário:** Função print para exibir algo na tela.

- `print (f"O custo atual é de {custo}")`  
  **Comentário:** f-strings para interpolação de variáveis.


### Dicas

- Use comentários para explicar partes importantes do código.
- Comentários não são executados pelo Python, servem apenas para documentação.
- Prefira comentários claros