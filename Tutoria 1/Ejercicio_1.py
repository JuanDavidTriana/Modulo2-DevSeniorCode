"""Clase `Libro`: Crea una clase llamada `Libro` que tenga los atributos: Título y Autor. Implementa un método `descripcion` que devuelva un texto como: `"El libro [Título] fue escrito por [Autor]."`"""

class Libro:
    # Atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    # Metodos
    def descripcion(self):
        return f"El libro {self.titulo} fue escrito por {self.autor}." 
    
    
libro1 = Libro("El señor de los anillos", "JRR Tolkien")
libro2 = Libro("Harry Potter y la piedra filosofal", "J.K Rowling")

print(libro2.descripcion())