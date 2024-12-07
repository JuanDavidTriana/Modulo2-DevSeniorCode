from abc import ABC, abstractmethod

class FigurasGeomatrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
class Circulo(FigurasGeomatrica):
    def __init__(self,radio):
        self.radio = radio
        
    def area(self):
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio
    
class Cuadraro(FigurasGeomatrica):
    def __init__(self,lado):
        self.lado = lado
        
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado

def main(): 
    figuras = [
        Circulo(5),
        Circulo(6),
        Cuadraro(5),
        Cuadraro(2)
    ]

    for figura in figuras:
        print(f"Area: {figura.area()}, Perimetro: {figura.perimetro()}")

if __name__ == "__main__":
    main()