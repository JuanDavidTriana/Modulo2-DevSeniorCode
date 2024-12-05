#Ejercicio: Agrega un método `mostrar_info` a `Coche` para mostrar los detalles del vehículo.  

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def mostar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Puertas: {self.puertas}")


Coche1 = Coche("Ford", "Mustang",4)
Coche1.mostar_info()
