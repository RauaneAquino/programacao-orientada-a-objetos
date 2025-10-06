class Aluno:
    def __init__(self, nome:str, nota1:float, nota2:float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2)/2    
        return media

    def mostrar_aprovacao(self):
        self.media = self.calcular_media()
        print(f"{self.nome} a sua média é {self.media}")
        if self.media >= 7:
            print("Você foi Aprovado")
        else:
            print("Você foi Reprovado")    


aluno1 = Aluno("Gerson", 7.5, 5.0) 
aluno1.calcular_media() 
aluno1.mostrar_aprovacao ()

aluno2 = Aluno("Ana", 8.0, 9.0) 
aluno2.calcular_media() 
aluno2.mostrar_aprovacao ()     