class Animal:
    def __init__(self, especie:str, som:str):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(f"O (a) {self.especie} faz {self.som}")    


animal1 = Animal("Gato", "Miau miau")
animal1.emitir_som()        
        