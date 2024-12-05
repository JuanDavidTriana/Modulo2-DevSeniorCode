#Ejercicio: Crea una clase `Vehiculo` con atributos `marca` y `modelo`. Luego, crea una clase `Coche` que herede de `Vehiculo` y agrega un atributo `puertas`.  

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
class Coche(Vehiculo):
    def ver_marca(self):
        return self.marca

Coche1 = Coche("Ford", "Mustang")

print(Coche1.ver_marca())
