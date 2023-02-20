class Personaje:
    
    #atributos personaje
    especie = "Humano"
    nombre = "Jerry"
    altura = "2.80"
    
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
        print("el arma tiene"+ cargador + "balas")