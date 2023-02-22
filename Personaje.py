class Personaje:
    
    #definimos el construcotr de personaje
    def __init__(self,esp,nom,alt):
      self.especie = esp
      self.nombre = nom
      self.altura = alt
    
    #Metodo Personaje 
    def correr(self,status):
        if(status):
            print("el personaje"+ self.nombre + " esta corriendo")
        else:
            print("el personaje"+ self.nombre + " se detuvo")

    def lanzarGranadas(self):
        print("el personaje"+ self.nombre + " lanzo una granada")
    
    def recargarArma(self,municion):
        cargador = 10
        cargador = cargador + municion
        print("el arma tiene"+ str(cargador)+ "balas")