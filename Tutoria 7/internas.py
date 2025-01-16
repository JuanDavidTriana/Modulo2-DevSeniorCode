class Externa:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    class Interna:
        def __init__(self,externa):
            self.externa = externa
            
        def mostar_mensaje(self):
            print(f"Mensaje desde clase externa {self.externa.mensaje}")
            
externa = Externa("Hola desde la clase externa")
interna = Externa.Interna(externa)
interna.mostar_mensaje()