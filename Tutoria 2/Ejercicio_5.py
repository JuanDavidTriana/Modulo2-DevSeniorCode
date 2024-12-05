#Ejercicio: Ejercicio: Modifica la clase `CuentaBancaria` para usar decoradores `@property` y `@setter` en el atributo `_saldo`.  

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, cantidad):
        if cantidad > 0:
            self.__saldo = cantidad
        else:
            print("La cantidad no es valida")
            
    def depositar(self, cantidad):
        
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de {cantidad} exitoso. Saldo actual es de : {self.__saldo}")
        else:
            print("La cantidad no es valida")
            
    def consultar_saldo(self):
        print(f"El saldo actual es de : {self.__saldo}")

CuentaJuanDavid = CuentaBancaria(1000)
CuentaJuanDavid.consultar_saldo()
CuentaJuanDavid.depositar(500)
CuentaJuanDavid.saldo = 500
print(CuentaJuanDavid.saldo)
CuentaJuanDavid.saldo = -100

