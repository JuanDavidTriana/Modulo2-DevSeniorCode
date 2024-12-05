class PublicExample:
    def __init__(self, saldo):
        self.public_atribute = "Soy publico"
        self._protected_atribute = "Soy protegido"
        self.__private_atribute = "Soy privado"
        self.__saldo = saldo
        
    def public_method(self):
        return "Este metodo es publico"
    
    def _protected_method(self):
        return "Este metodo es protegido"
    
    def __private_method(self):
        return "Este metodo es privado"
    
    def consultar_saldo(self):
        return f"Saldo acual: {self.__saldo}"
    
obj = PublicExample(50000)

print("------------Publico--------------")
print(obj.public_atribute) 
print(obj.public_method())
print("------------Protegido--------------")
print(obj._protected_atribute) 
print(obj._protected_method())
print("------------Privado--------------")
print(obj.consultar_saldo())
#print(obj.__private_atribute)
#print(obj.__private_method())
