from abc import ABC, abstractmethod

class vehiculo(ABC):
    @abstractmethod
    def create(self):
        pass
    
class carro(vehiculo):
    def create(self):
        return "Se creo un carro"
    
class moto(vehiculo):
    def create(self):
        return "Se creo una moto"
    
class vehiculoFactory:
    @staticmethod
    def get_vehiculo(vehiculo_tipo):
        if vehiculo_tipo == "carro":
            return carro()
        elif vehiculo_tipo == "moto":
            return moto()
        else:
            raise ValueError("Tipo de vehiculo desconocido")
        
try:
    factory = vehiculoFactory()
    
    car = factory.get_vehiculo("carro")
    print(car.create())
    
    motorcycle = factory.get_vehiculo("moto")
    print(motorcycle.create())
    
    unknown = factory.get_vehiculo("cicla")
except ValueError as e:
    print(e)
    