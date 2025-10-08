class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_livros = []

    def adicionar_livro(self, titulo):
        self.lista_de_livros.append(titulo)  

    def listar_livros(self):
        print(f"Biblioteca: {self.nome}\nLista de livros")
        print(self.lista_de_livros)     

titulo1 = ("O Peregrino")    
titulo2 = ("O pequeno Príncipe")
titulo3 = ("Heróis da fé")

minha_biblioteca = Biblioteca("Biblioteca Pessoal")
minha_biblioteca.adicionar_livro(titulo1)
minha_biblioteca.adicionar_livro(titulo2)
minha_biblioteca.adicionar_livro(titulo3)
minha_biblioteca.listar_livros()