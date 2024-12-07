#Polimosfirmo a traves de metodos comumes en diferentes clases

class Gato:
    def sonido(self):
        return "Miau miau"
    
class Carro:
    def sonido(self):
        return "Piii piii"
    

def hacer_sonido(objeto):
    print(objeto.sonido())
    
#Instaciar 
mi_gato = Gato()
mi_carro = Carro()

#Uso del poli
print(f"Mi gato Luna hace el siguete sonido:")
hacer_sonido(mi_carro)