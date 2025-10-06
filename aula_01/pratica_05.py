class ContaBancaria:
    def __init__(self, titular:str, saldo:float):
        saldo = 0
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
           self.saldo += valor
           print(f"Depósito de R${valor:.2f} feito com sucesso")
        else:
            print("O valor do depósito deve ser positivo")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} feito com sucesso")   
        else:
            print("Saldo insuficiente ou valor inválido para saque")   

    def mostrar_saldo(self):
       print(f"Saldo atual de {self.titular}: R${self.saldo}")   


conta1 = ContaBancaria("Rauane", 0)
conta1.mostrar_saldo()  
conta1.depositar(500)
conta1.sacar(200)
conta1.mostrar_saldo()

