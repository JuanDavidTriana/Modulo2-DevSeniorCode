class Libro:
    def __init__(self,nombre,autor,genero):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        
    def agregar_un_libro(self):
        print(f"Libro agregado con exito")
        
class LibroFantasia(Libro):
    def agregar_un_libro(self):
        print("Libro de fantasia agregado")


libro1 = LibroFantasia("Harry Potter","J.K","Magia")
libro2 = Libro("Harry Potter","J.K","Magia")

libro1.agregar_un_libro()
libro2.agregar_un_libro()