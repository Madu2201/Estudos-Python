# 📘 Funções em Python:

### 🧮 Função `sum()`

A função `sum()` é usada para somar todos os elementos de um iterável (como listas, tuplas ou conjuntos).

### 📌 Sintaxe:
```python
sum(iterável, início)

- Exemplo¹
numeros = [1, 2, 3, 4]
print(sum(numeros))  # Saída: 10

# Soma com valor inicial
print(sum(numeros, 10))  # Saída: 20
```

## 🔧 Outras funções úteis em Python

### **Função | Descrição:**

`len()`	        Retorna o número de itens em um objeto (como lista, string, etc.)

`max()`	        Retorna o maior valor de um iterável

`min()`	        Retorna o menor valor de um iterável

`sorted()`	    Retorna uma lista ordenada a partir de um iterável

`enumerate()`   Retorna pares (índice, valor) ao iterar sobre uma sequência

`zip()`	        Junta múltiplas listas em pares (ou tuplas) correspondentes

`map()`	        Aplica uma função a cada item de um iterável

`filter()`	    Filtra itens de um iterável com base em uma função que retorna True



## 🧰 Operações Comuns em Listas

### **Operação | Descrição	| Exemplo**

`in`	                    Verifica se um item está na lista       `"iphone" in produtos → True`

`append()`	                Adiciona item ao final da lista	        `produtos.append("macbook")`

`insert(indice, valor)`	    Insere item em posição específica	    `produtos.insert(1, "celular")`

`remove(valor)`         	Remove item pelo valor	                `produtos.remove("macbook")`

`pop(indice)`	            Remove item pelo índice	                `precos.pop(-1)`

`count(valor)`	            Conta quantas vezes o item aparece	    `produtos.count("airpod") → 1`

`sort()`	                Ordena lista em ordem crescente	        `precos.sort()`

`reverse()`	                Inverte a ordem da lista	            `precos.reverse()`

`lista[indice] = valor`	    Altera o valor de um item da lista	    `precos[0] = 4500`

`lista[indice] *= número`	Aplica operação mát sobre item da lista	`precos[0] *= 1.1`



## Dicas Extras

- `iterável`:  qualquer objeto que possa ser percorrido (como uma lista de números).
- `início (opcional)`: valor inicial da soma. Se fornecido, será adicionado ao total.

