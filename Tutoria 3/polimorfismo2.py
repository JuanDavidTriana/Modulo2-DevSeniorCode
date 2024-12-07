#Polimorfismo con heriencia y metodos sobrescritos
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    
class Perro(Animal):
    def sonido(self):
        return "Guau guau"
    
class Gato(Animal):
    pass
    
mi_gato = Gato()
mi_perro = Perro()

print(mi_gato.sonido())