#Ejercicio: Crea una clase `CuentaBancaria` con un atributo privado `_saldo`. Agrega métodos para depositar y retirar dinero, asegurándote de que no se permita un saldo negativo.  

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        
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
