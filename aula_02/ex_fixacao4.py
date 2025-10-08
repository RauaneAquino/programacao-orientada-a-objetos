class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R${self.preco})"    

class CarrinhoDeCompras:
    def __init__(self):
        self.listaProdutos = []

    def adicionar(self, produto):
        self.listaProdutos.append(produto)

    def calcular_total(self):
        total = 0.0
        for produto in self.listaProdutos:
            total += produto.preco    
        return total
    
    def __str__(self):
        produtos_str = "\n".join([str(p) for p in self.listaProdutos])
        return f"Itens no Carrinho:\n{produtos_str}\nTotal: R${self.calcular_total()}"
    


produto1 = Produto("Creme de cabelo", 12.00)
produto2 = Produto("Caderno", 20.00)
produto3 = Produto("Touca Cetim", 15.00)

meu_carrinho = CarrinhoDeCompras()
meu_carrinho.adicionar(produto1)
meu_carrinho.adicionar(produto2)
meu_carrinho.adicionar(produto3)
print(meu_carrinho)

total_compra = meu_carrinho.calcular_total()
print(f"O total da compra é: {total_compra}")