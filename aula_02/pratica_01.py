class Prato:
    def __init__(self, nome: str, preco:float, disponibilidade: bool):
        self.nome = nome
        self.preco = preco
        self.disponibilidade = disponibilidade

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Preço R$: {self.preco}")  
        status = "Disponível" if self.disponibilidade else "Indisponível"
        print(f"Status: {status}")

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O novo preço é {self.preco}")


    def indisponibilizar(self):
        if self.disponibilidade == False:
            print(f"O prato {self.nome} está Indisponível")    
            

class Pedido:
    def __init__(self):
        self.pratos = []

    def adicionar_pratos(self, prato:Prato):
        if prato.disponibilidade:
            self.pratos.append(prato)
            print(f"O prato {prato.nome} foi adicionado")
        else:
            print(f"Não pode adicionar o prato {prato.nome} não está disponível")   

    def total(self):
        soma = sum(Prato.preco for prato in self.pratos)
        print(f"Total do pedido: R$ {soma}")
        return soma

prato1 = Prato("Frango frito", 18.00,True)
prato2 = Prato("Bisteca", 25.00, True)
prato3 = Prato("Peixe assado", 45.00, False) 

prato1.exibir()
prato2.exibir()
prato3.exibir()

prato1.alterar_preco(20.00)
prato2.indisponibilizar()

pedido = Pedido()
pedido.adicionar_pratos(prato1)
pedido.adicionar_pratos(prato2)


pedido.total()