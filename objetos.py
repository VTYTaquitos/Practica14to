
from Personaje import * #si quiero importar todo se pone el asterisco y si es solo uno se pone especificamente


#1.Solicitar datos
print("")
print("####### DATOS Heroe #####")
especieH=input("Escribe la especie del heroe: ")
nombreH=input("Escribe el nombre del heroe: ")
alturaH=float(input("Escribe la altura del heroe: "))
recargaH= int(input("Cuantas balas recargas al heroe: "))

print("")
print("####### DATOS Villano #####")
especieV=input("Escribe la especie del villano: ")
nombreV=input("Escribe el nombre del villano: ")
alturaV=float(input("Escribe la altura del villano: "))
recargaV= int(input("Cuantas balas recargas al villano: "))

#2 Crear objeto de clase personaje
heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3 Usar atributos y metodos
print("")
print("####### Objeto Heroe #####")
print("El personaje se llama: "+ heroe.nombre)
print("Pertenece a la especie: "+ heroe.especie)
print("Tiene un altura de: "+ str(heroe.altura))
heroe. correr (True)
heroe. lanzarGranadas()
heroe. recargarArma(recargaH)

print("")
print("####### Objeto Villano #####")
print("El personaje se llama: "+ villano.nombre)
print("Pertenece a la especie: "+ villano.especie)
print("Tiene un altura de: "+ str(villano.altura))
villano. correr (True)
villano. lanzarGranadas()
villano. recargarArma(recargaV)
