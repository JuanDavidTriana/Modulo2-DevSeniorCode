#Ejercicio: Ejercicio: Agrega un método protegido `_calcular_interes` en la clase `CuentaBancaria` que calcule un 5% de interés sobre el saldo actual.

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def _cancular_interes(self):
        interes = self.__saldo * 0.05
        print(f"El interes es de {interes}")

    def depositar(self, cantidad):
        
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de {cantidad} exitoso. Saldo actual es de : {self.__saldo}")
        else:
            print("La cantidad no es valida")
            
    def consultar_saldo(self):
        print(f"El saldo actual es de : {self.__saldo}")

CuentaJuanDavid = CuentaBancaria(100)
CuentaJuanDavid.depositar(50)
CuentaJuanDavid.consultar_saldo()
CuentaJuanDavid._cancular_interes()
