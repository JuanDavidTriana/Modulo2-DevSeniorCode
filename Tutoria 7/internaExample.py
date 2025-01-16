class CuentaBanco: # Clase Externa 
    def __init__(self, titular,saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    class Transaccion: # Clase Interna
        def __init__(self, cuenta,monto, tipo):
            self.cuenta= cuenta
            self.monto = monto
            self.tipo = tipo
            
        def ejecutar(self):
            if self.tipo == "deposito":
                self.cuenta.saldo += self.monto
            elif self.tipo == "retiro" and self.cuenta.saldo >= self.monto:
                self.cuenta.saldo -= self.monto
            else:
                print("Fondos insuficientes para la transaccion")
            print(f"Saldo actual: {self.cuenta.saldo}")
            
cuenta = CuentaBanco("Juan David", 1000)
deposito = cuenta.Transaccion(cuenta,500,"deposito")
deposito.ejecutar()

retiro = cuenta.Transaccion(cuenta,400,"retiro")
retiro.ejecutar()