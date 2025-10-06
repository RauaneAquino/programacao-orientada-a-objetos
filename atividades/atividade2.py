class Paciente:
    def __init__(self, nome:str, idade:int, cpf:str, doenca:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.doenca = doenca

    def exibir_dados(self):
        print("Paciente: ")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}") 
        print(f"CPF: {self.cpf}") 
        print(f"Doença: {self.doenca}") 


    def atualizar_doenca(self):
        self.doenca = input("Informe a nova doença: ")  



paciente1 = Paciente("Roberto", 48, "012.456.987-01", "Diabetes")
paciente1.exibir_dados()
paciente1.atualizar_doenca()
paciente1.exibir_dados()

paciente2 = Paciente("Maria Aparecida", 62, "005.654.964-03", "Hipertensão")
paciente2.exibir_dados()




        
                 