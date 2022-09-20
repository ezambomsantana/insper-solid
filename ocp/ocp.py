

class Animal:
    def __init__(self, name: str, especie: str):
        self.especie = especie
        self.name = name

    def voa(self) -> bool:
        if self.especie == 'ave':
            return True
        return False

    def nada(self) -> bool:
        if self.especie == 'peixe':
            return True
        return False

    def anda(self) -> bool:
        if self.especie == 'mamifero' or self.especie == 'ave':
            return True
        return False
    
    def get_name(self) -> str:
        return name


p = Animal('gato', 'mamifero')
def verificaAnimalAnda(animal:Animal):
    if animal.anda():
        print('anda')
    else:
        print('nao anda')
