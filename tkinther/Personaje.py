class Personaje:
    
    #definimos el construcotr de personaje y los encapsulamos 
    def __init__(self,esp,nom,alt):
      self.__especie = esp
      self.__nombre = nom
      self.__altura = alt
    
    #Metodo Personaje 
    def correr(self,status):
        if(status):
            print("el personaje "+ self.__nombre + " esta corriendo")
        else:
            print("el personaje "+ self.__nombre + " se detuvo")

    def lanzarGranadas(self):
        print("el personaje "+ self.__nombre + " lanzo una granada")
    
    def recargarArma(self,municion):
        cargador = 10
        cargador = cargador + municion
        print("el arma tiene "+ str(cargador)+ " balas")
    
    def __pensar(self):
        print (" Estoy pensando.................... ")
        
    #Declarar Getters y Setters de atibutos
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self.__nombre= nom
        
    def getEspecie(self):
        return self.__especie
    def setEspecie(self,esp):
        self.__especie= esp
        
    def getAltura(self):
        return self.__altura
    def setAltura(self,alt):
        self.__altura= alt