from abc import ABC, abstractmethod

#Clase abstracta
class Empleado(ABC):
    def __init__(self,nombre, id, salario_base):
        self._nombre = nombre
        self._id = id
        self._salario_base = salario_base
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def id(self):
        return self._id
    
    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self,nuevo_salario):
        if nuevo_salario > 0:
            self._salario_base = nuevo_salario
        else:
            raise ValueError("El salario debe ser mayor a 0")
        
    @abstractmethod
    def calcular_bono(self):
        pass
    
    def __str__(self):
        return f"Empleado: {self._nombre}, id: {self._id}, salario base: {self._salario_base}"

class Desrollador(Empleado):
    def calcular_bono(self):
        return self._salario_base * 0.10

class Diseñador(Empleado):
    def calcular_bono(self):
        return self._salario_base * 0.05

class Gerente(Empleado):
    def calcular_bono(self):
        return 500.0

if __name__ == "__main__":
    dev = Desrollador("Santiago", 101, 5000)
    designer = Diseñador("Juan David",102,4000)
    manager = Gerente("John", 103, 8000)
    
    empleados = [dev,designer,manager]
    
    for empleado in empleados:
        print(empleado)
        print(f"Bono: {empleado.calcular_bono()}")
        print("********************************")