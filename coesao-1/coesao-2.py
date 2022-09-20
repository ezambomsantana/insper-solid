
class Carro:
    
    def __init__(self, placa: str, modelo: str):
        self.placa = placa
        self.modelo = modelo
    
    def get_name(self) -> str:
        return name

class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: str, carro: Carro):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.carro = carro
    
    def get_name(self) -> str:
        return name

c = Carro('XYZ', 'Onyx')

p = Pessoa('Eduardo', 36, 'Rua ABC', c)
print(p.carro.placa)
    