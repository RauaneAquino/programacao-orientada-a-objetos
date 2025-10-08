class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self): 
        print("-" * 30)
        print(f"Aluno(a): {self.nome}\nIdade: {self.idade}\nCurso: {self.curso}")  

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_alunos = []

    def adicionar_aluno(self, aluno):
        self.lista_de_alunos.append(aluno) 
        print(f"- {aluno.nome} matriculado na escola {self.nome}") 

    def listar_alunos(self):
        print(f"Lista de Alunos da Escola {self.nome}")
        for aluno in self.lista_de_alunos:
            aluno.apresentar()
            print("-" * 30)    

aluno1 = Aluno("Rauane", 27, "Informática") 
aluno2 = Aluno("Felipe", 23, "Secretariado")
aluno1.apresentar()      
aluno2.apresentar()
escola1 = Escola("Escola Vasco Vasques")
escola1.adicionar_aluno(aluno1)
escola1.adicionar_aluno(aluno2)
escola1.listar_alunos()