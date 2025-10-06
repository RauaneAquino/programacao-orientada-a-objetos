class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

pessoa1 = Pessoa("Rauane", 27)
pessoa2 = Pessoa("Barbara", 21)    

pessoa1.mostrar()
pessoa2.mostrar()
