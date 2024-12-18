import json

class SistemaGuardado:
    
    __intance = None
    
    @staticmethod
    def get_instance():
        if SistemaGuardado.__intance is None:
            SistemaGuardado.__intance = SistemaGuardado()
        return SistemaGuardado.__intance
    
    def __init__(self):
        self.archivo_gurdado = "guardado.bat"
        
    def guardar_juego(self, dato_a_guardar):
        with open(self.archivo_gurdado, "w") as f:
            json.dump(dato_a_guardar,f, indent=2)
            
    def cargar_juego(self):
        with open(self.archivo_gurdado, "r") as f:
            return json.load(f)
        

class Jugador():
    
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
    
    def serializar(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel
        }
        
    @classmethod   
    def deserializar(self, data):
        return self(data["nombre"], data["nivel"])
        
def cargar_partida():
    guardo = SistemaGuardado.get_instance()
    datos_guardados = guardo.cargar_juego()
    jugador = Jugador.deserializar(datos_guardados)

"""        
jugador1 = Jugador("Juan David",25)
guardando = SistemaGuardado.get_instance()
guardando.guardar_juego(jugador1.serializar())
"""
guardando = SistemaGuardado.get_instance()
datos_cargados = guardando.cargar_juego()
jugardor_cargado = Jugador.deserializar(datos_cargados)
print(jugardor_cargado.nombre)
