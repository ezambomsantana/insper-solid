

class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: str, placa_carro: str, modelo_carro: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.placa_carro = placa_carro
        self.modelo_carro = modelo_carro
    
    def get_name(self) -> str:
        return name


    def save() -> boolean:
        pass #imagine um método salvando alguma coisa no DB


p = Pessoa('Eduardo', 36, 'Rua ABC', 'XYZ', 'Onyx')
print(p.placa_carro)
    