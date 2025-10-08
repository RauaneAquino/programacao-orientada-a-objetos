class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.cardapio = []

    def adicionar_prato(self, prato):
        self.cardapio.append(prato)

    def listar_cardapio(self):
        print(f"Restaurante {self.nome}\nCardápio do dia")
        print(self.cardapio)

    def atender_cliente(self, nome_cliente, prato_pedido):
            if prato_pedido in self.cardapio:
                print(f"{nome_cliente} o seu pedido de {prato_pedido} está confirmado")
            else:
                print(f"{nome_cliente}, o prato {prato_pedido} não existe")    

restaurante1 = Restaurante("Sabor Caseiro")
restaurante1.adicionar_prato("Galinha caipira")
restaurante1.adicionar_prato("Carne Guisada")
restaurante1.adicionar_prato("Frango Frito")
restaurante1.listar_cardapio()
restaurante1.atender_cliente("Renata", "Galinha caipira")
restaurante1.atender_cliente("Maria", "Ovo frito")