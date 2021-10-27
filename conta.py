class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("saldo de R${} do titular {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, saque):
        return  saque <= (self.__limite + self.__saldo)

    def saca(self, saque):
        if(self.__pode_sacar(saque)):
            self.__saldo -= saque
        else:
            print("O valor do saque de R${} ultrapassou o limite".format(saque))

    def deposita(self, deposito):

        self.__saldo += deposito

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {"BB": "001", "caixa": "104", "Bradesco": "237"}
