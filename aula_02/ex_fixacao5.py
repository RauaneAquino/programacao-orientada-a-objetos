class Passageiro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"    

class Onibus:
    def __init__(self, linha, capacidade):
        self.linha = linha
        self.capacidade = capacidade
        self.lista_passageiros = []    

    def __str__(self):
        return f"{self.linha} {self.capacidade}"    

    def embarcar(self, passageiro):
        if len(self.lista_passageiros) < self.capacidade:
            self.lista_passageiros.append(passageiro)
        else:
            print("Erro! Capacidade excedida ")    
    

    def listar_passageiros(self):
        print(f"{self.linha}\nPassageiros a bordo ")
        if not self.lista_passageiros:
            print("Nenhum passageiro a bordo.")
            return
        for passageiro in self.lista_passageiros:
            print(f" - {passageiro}")



passageiro1 = Passageiro("Ana", 18)
passageiro2 = Passageiro("Rafael", 37)
passageiro3 = Passageiro("Ivone", 52)
onibus1 = Onibus("676 - Centro/Bairro", 2)

onibus1.embarcar(passageiro1)
onibus1.embarcar(passageiro2)
onibus1.embarcar(passageiro3)
onibus1.listar_passageiros()
