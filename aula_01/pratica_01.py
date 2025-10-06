class Ar_Condicionado:
    def __init__(self, tipo:str, cor:str, potencia:int, velocidade: float, temperatura:str, controle: bool, modo: str):
        self.tipo = tipo
        self.cor = cor
        self.potencia = potencia
        self.velocidade = velocidade
        self.temperatura = temperatura
        self.controle = controle
        self.modo = modo

    def ligar(self):
        print(f"{self.modo} ligado.")

    def desligar(self):
        print(f"{self.modo} desligado.")

    def aumentar_temperatura(self):
        print(f"{self.temperatura} aumentando temperatura.")
    def diminuir_temperatura(self):
        print(f"{self.temperatura} diminuindo temperatura.")    

    def possui_controle(self):
        print(f"{self.controle} possui controle") 

meu_ar = Ar_Condicionado("Split", "Branco", 9000, "Baixo", 18, True, "Ligado")           

meu_ar.ligar()
meu_ar.possui_controle()
meu_ar.aumentar_temperatura()
meu_ar.diminuir_temperatura()
meu_ar.desligar()
    
