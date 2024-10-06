
class Conta:

    def __init__(self,numero,saldo = 0.0) :
        self.__numero = numero
        self.saldo = saldo
    

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self,saldo):
        self.__saldo = saldo
    saldo = property(get_saldo, set_saldo)
    

    def depositar(self,valor) :
        self.valor = valor
        self.set_saldo(valor)
       

    def sacar(self,valor) :
        self.valor = valor
        if(self.saldo<self.valor) :
            print("Dinheiro insuficiente!")
        else :
            self.set_saldo(self.saldo - self.valor)


class ContaCorrente(Conta):
    def __init__(self,numero,taxa):
         super().__init__(numero)
         self.taxa = taxa

    def cobrar_taxa(self) :
       self.set_saldo((self.saldo - self.taxa))
       


class ContaPoupanca(Conta) :
    def __init__(self,numero,juros):
         super().__init__(numero)
         self.juros = juros
    def aplicar_juros(self):
        self.set_saldo((self.saldo)+(self.juros *self.saldo))