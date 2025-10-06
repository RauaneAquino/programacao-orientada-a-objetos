class Aluno:
    def __init__(self, nome:str, nota1:float, nota2:float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2)/2
        return media
        
    def mostrar_resultado(self):
        media = self.calcular_media()
        print(f"A média do aluno(a) {self.nome} é ", media)
        if media >= 7:
            print("Aluno Aprovado! ")
        else:
            print("Aluno Reprovado!")    



aluno1 = Aluno("Mário", 6.0, 9.5)
aluno1.calcular_media()   
aluno1.mostrar_resultado()  

aluno2 = Aluno("Rebeca", 4.0, 5.0)
aluno2.calcular_media()   
aluno2.mostrar_resultado()  