class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        
    def mover(self):
        print("El vehiculo he comenenzado a moverse")

class Coche(Vehiculo):
    def __init__(self,marca, motor, ruedas):
        super().__init__(marca)
        self.motor = motor
        self.ruedas = ruedas 
        
    def iniciar_viaje(self):
        self.motor.encender()
        for rueda in self.ruedas:
            rueda.girar()
        self.mover()
    
    def mover(self):
        print("El coche he comenenzado a moverse")
        
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def encender(self):
        print(f"El Motor de tipo {self.tipo} se he encendido")
    
class Rueda:
    def __init__(self, tamano):
        self.tamano = tamano
        
    def girar(self):
        print(f"la rueda de tamaño {self.tamano} esta girando")
        
motor_depertivo = Motor("V10")

tipo_ruedas= int(input("Elija el tipo de ruedas que va a usar (10-50):"))

ruedas_pequeñas = [Rueda(tipo_ruedas),Rueda(tipo_ruedas),Rueda(tipo_ruedas),Rueda(tipo_ruedas)]      

coche_deportivo = Coche("Ferrary",motor_depertivo,ruedas_pequeñas)
coche_deportivo.iniciar_viaje()