# 🐾 Sistema de Adoção de Animais — Explicação do Código

Este projeto simula um sistema simples de adoção de animais usando programação orientada a objetos em Python. Ele é composto por três classes principais: `Animal`, `Cachorro`/`Gato` (subclasses) e `Usuario`.

[Ver código completo](/codigos/poo.py)

---

## 1. Classe Base: `Animal`

```python
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def interagir(self):
        print(f"{self.nome} está feliz em te ver!")
```

*Representa qualquer animal genérico.*

*Possui atributos básicos: nome e especie.*

*O método interagir() imprime uma mensagem padrão de interação.*

## 2. Subclasses: Cachorro e Gato

```python
class Cachorro(Animal):
    def interagir(self):
        print(f"{self.nome} abana o rabo e late: Au au!")

class Gato(Animal):
    def interagir(self):
        print(f"{self.nome} ronrona e mia: Miau!")
```

*Ambas herdam da classe Animal.*

**Sobrescrevem o método interagir() para comportamentos específicos:**

*Cachorro: abana o rabo e late.*

*Gato: ronrona e mia.*

## 3. Classe Usuario

```python
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self._animais = []

    def adotar(self, animal):
        self._animais.append(animal)
        print(f"{self.nome} adotou {animal.nome} ({animal.especie})!")

    def listar_animais(self):
        if not self._animais:
            print("Nenhum animal adotado ainda.")
        else:
            print("Animais adotados:")
            for animal in self._animais:
                print(f"- {animal.nome} ({animal.especie})")

    def brincar_com_animais(self):
        for animal in self._animais:
            animal.interagir()
```

*Representa um usuário que pode adotar e interagir com animais.*

**Métodos:**

*adotar(animal): adiciona um animal à lista.*

*listar_animais(): exibe os animais adotados.*

*brincar_com_animais(): chama o método interagir() de cada animal.*

---

## 🧪 Simulação Interativa

```python
usuario = Usuario("Fernanda")

rex = Cachorro("Rex", "Cão")
mimi = Gato("Mimi", "Gato")

usuario.adotar(rex)
usuario.adotar(mimi)

usuario.listar_animais()
usuario.brincar_com_animais()
```

---

## 💻 Saída Esperada:

```
Código
Fernanda adotou Rex (Cão)!
Fernanda adotou Mimi (Gato)!
Animais adotados:
- Rex (Cão)
- Mimi (Gato)
Rex abana o rabo e late: Au au!
Mimi ronrona e mia: Miau!
```

---

# ✅ Conclusão

**Este código é um exemplo didático de:**

**Herança e polimorfismo em Python.**

**Encapsulamento de dados.**

**Interação entre objetos.**
