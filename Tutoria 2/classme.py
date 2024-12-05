class Persona:
    cantidad_personas = 0
    total_saldo = 0
    
    def __init__(self, nombre,saldo):
        self.nombre = nombre
        self.saldo = saldo
        Persona.cantidad_personas += 1
        Persona.total_saldo += saldo
        
    @classmethod
    def total_personas(cls):
        print("Cantidad de personas:", cls.cantidad_personas)
        
    @classmethod
    def consultar_saldos_totales(cls):
        print("Total de saldo:", cls.total_saldo)
    
persona1 = Persona("Juan",800)
persona2 = Persona("Pedro",200)
print(persona1.total_personas())
print(persona1.consultar_saldos_totales())
