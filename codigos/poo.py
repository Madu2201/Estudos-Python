# 🐾 Classe base que representa um animal genérico
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome          # Nome do animal
        self.especie = especie    # Espécie do animal

    def interagir(self):
        # Método genérico de interação
        print(f"{self.nome} está feliz em te ver!")

# 🐶 Subclasse que representa um cachorro
class Cachorro(Animal):
    def interagir(self):
        # Sobrescreve o método interagir para comportamento específico de cachorro
        print(f"{self.nome} abana o rabo e late: Au au!")

# 🐱 Subclasse que representa um gato
class Gato(Animal):
    def interagir(self):
        # Sobrescreve o método interagir para comportamento específico de gato
        print(f"{self.nome} ronrona e mia: Miau!")

# 👤 Classe que representa um usuário que pode adotar animais
class Usuario:
    def __init__(self, nome):
        self.nome = nome              # Nome do usuário
        self._animais = []            # Lista privada de animais adotados

    def adotar(self, animal):
        # Adiciona um animal à lista de adotados
        self._animais.append(animal)
        print(f"{self.nome} adotou {animal.nome} ({animal.especie})!")

    def listar_animais(self):
        # Lista todos os animais adotados
        if not self._animais:
            print("Nenhum animal adotado ainda.")
        else:
            print("Animais adotados:")
            for animal in self._animais:
                print(f"- {animal.nome} ({animal.especie})")

    def brincar_com_animais(self):
        # Interage com todos os animais adotados
        for animal in self._animais:
            animal.interagir()

# 🧪 Simulação interativa
usuario = Usuario("Fernanda")         # Cria um usuário chamado Fernanda

rex = Cachorro("Rex", "Cão")          # Cria um cachorro chamado Rex
mimi = Gato("Mimi", "Gato")           # Cria uma gata chamada Mimi

usuario.adotar(rex)                   # Fernanda adota Rex
usuario.adotar(mimi)                  # Fernanda adota Mimi

usuario.listar_animais()              # Lista os animais adotados
usuario.brincar_com_animais()         # Interage com os animais
