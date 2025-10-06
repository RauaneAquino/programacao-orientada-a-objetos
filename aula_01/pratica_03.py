class Cachorro:
    def __init__(self, nome:str, raca:str):
        self.nome = nome
        self.raca = raca


    def latir(self):
        print(f"Au Au! O cachorro {self.nome} está latindo.")    

cachorro1 = Cachorro("Bob", "Caramelo")
cachorro1.latir()        