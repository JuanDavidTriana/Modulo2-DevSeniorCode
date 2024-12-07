class mamifero:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def alimentar(self):
        return f"{self.nombre} se esta alimentando"

class volador:
    def volar(self):
        return f"{self.nombre} esta volando"

class murcielago(mamifero,volador):
    def __init__(self, nombre):
        super().__init__(nombre)
        
bat = murcielago("Betty")

print(bat.volar())
print(bat.alimentar())
