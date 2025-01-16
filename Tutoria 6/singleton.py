import sqlite3

class DatabaseConnection:
    
    _instances = {}


    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(DatabaseConnection,cls).__new__(cls,*args, **kwargs)
            cls._instances.connection = None
        return cls._instances
    
    """
    def __init__(self):
        self.connection = None
    """
    
    def connect(self, database_name):
        if self.connection is None:
            self.connection = sqlite3.Connection(database_name)
            print(f"Conectado a la base de datos {database_name}")
        else:
            print("Ya exite una conexion activa")
        return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("conexio cerrada")
            self.connection = None
        
db1 = DatabaseConnection()
connetion1 = db1.connect("mi_base_de_datos.db")

db2 = DatabaseConnection()
connetion2 = db2.connect("otra_base_de_datos.db")

print(db1 == db2)

db1.close_connection()
db2.close_connection()