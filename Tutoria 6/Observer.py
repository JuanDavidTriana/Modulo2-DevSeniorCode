class nuevoCanal:
    def __init__(self):
        self._suscriptor = []
        self._laters_mews = None
        
    def suscribir(self, suscribirse):
        self._suscriptor.append(suscribirse)
        
    def desuscribir(self, suscribirse):
        self._suscriptor.remove(suscribirse) 
        
    def notificacion(self):
        for sus in self._suscriptor:
            sus.update(self._laters_mews)
            
    def publicacion(self, news):
        self._laters_mews = news
        print(f"Notificacion publicada: {news}")
        self.notificacion()
        
class suscriptores:
    def __init__(self, name):
        self.name = name
        
    def update(self, news):
        print(f"{self.name} ha recibio la notificacion: {news}")
        
        
canalDevSeniorCode = nuevoCanal()

sus1 = suscriptores("Juan")
sus2 = suscriptores("Eder")
sus3 = suscriptores("Edison")

canalDevSeniorCode.suscribir(sus1)
canalDevSeniorCode.suscribir(sus2)

canalDevSeniorCode.publicacion("Tenemos tutoria el día de hoy")

canalDevSeniorCode.suscribir(sus3)

canalDevSeniorCode.publicacion("Tenemos tutoria 2 el día de hoy")

canalDevSeniorCode.desuscribir(sus3)

canalDevSeniorCode.publicacion("Tenemos tutoria 3 el día de hoy")