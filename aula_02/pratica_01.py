class Prato:
    def __init__(self, nome: str, preco:float, disponibilidade: bool):
        self.nome = nome
        self.preco = preco
        self.disponibilidade = disponibilidade

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Preço R$: {self.preco}")  


    def alterar_preco(self, novo_preco):
        self.preco = novo_preco


    def indisponibilizar(self):
        if self.disponibilidade == True:
            print(f"Disponível {self.nome}")    
        else:
            print("Indisponível")       


class Pedido:
    pratos = ["Carne", "Frango", "Peixe"]

    def total(self, soma):
        self.soma = 0
        self.soma = self.soma + self.preco

prato1 =         
