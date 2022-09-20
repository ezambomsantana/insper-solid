

class Animal:
    def __init__(self, name: str):
        self.name = name

    def voa(self) -> bool:
        return False

    def nada(self) -> bool:
        return False

    def anda(self) -> bool:
        return False
    
    def get_name(self) -> str:
        return name

class Peixe(Animal):
    def nada(self) -> bool:
        return True

class Mamifero(Animal):
    def anda(self) -> bool:
        return True

class Ave(Animal):
    def voa(self) -> bool:
        return True



def verificaAnimalAnda(animal:Animal):
    if animal.anda():
        print('anda')
    else:
        print('nao anda')

p = Mamifero('gato')
verificaAnimalAnda(p)