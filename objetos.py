
from Personaje import * #si quiero importar todo se pone el asterisco y si es solo uno se pone especificamente

#1 Crear objeto de clase personaje
heroe= Personaje()

#2 Usar atributos
print("El personaje se llama: "+ heroe.nombre)
print("Pertenece a la especie: "+ heroe.especie)
print("Tiene un altura de: "+ heroe.altura)

#3 Usar metodos 
heroe. correr (True)
heroe. lanzarGranadas()
heroe. recargarArma(87)
