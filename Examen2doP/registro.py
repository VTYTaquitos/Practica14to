from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from matricula import *

def generar():
    Nombre_E =  NomEn.get()
    ApePapa = ApePa.get()
    ApeMama = ApeMa.get()
    AñoNas = Nas.get()
    Carrera_E = Car.get()
   #print(Nombre_E, ApePapa, ApeMama, AñoNas, Carrera_E)
    Fmat.Crear(Nombre_E, ApePapa, ApeMama, AñoNas, Carrera_E)

Fmat = matricula()   

ventana= Tk()  
ventana.geometry("600x400")
ventana.title("Registro")

##Secciones
seccion1= Frame(ventana,bg= "black")
seccion1.pack(expand=True,fill='both')
seccion2= Frame(ventana,bg= "black")
seccion2.pack(expand=True,fill='both')
seccion3= Frame(ventana, bg="black")
seccion3.pack(expand=True,fill='both')

##Textos
txtinicio= Label(seccion1,text="Ingresa los datos ",bg= "black", fg="orange")
txtinicio.configure(font=("arial", 14))
txtinicio.place(width="650", height="80")
txtNo= Label(seccion2,text="Nombre:",bg= "black", fg="orange")
txtNo.configure(font=("arial",10))
txtNo.place(x=90,y=5)
txtPa= Label(seccion2,text="Apellido Paterno:",bg= "black", fg="orange")
txtPa.configure(font=("arial",10))
txtPa.place(x=90,y=25)
txtMa= Label(seccion2,text="Apellido Materno:",bg= "black", fg="orange")
txtMa.configure(font=("arial",10))
txtMa.place(x=90,y=45)
txtNa= Label(seccion2,text="Año de nacimiento:",bg= "black", fg="orange")
txtNa.configure(font=("arial",10))
txtNa.place(x=90,y=65)
txtCa= Label(seccion2,text="Carrera:",bg= "black", fg="orange")
txtCa.configure(font=("arial",10))
txtCa.place(x=90,y=85)

# boton
botonIngresar = Button(seccion3,text="Generar", fg= "black", bg="orange", command= generar)
botonIngresar.place(x=90, y=40)

# Colocamos los campos
NomEn= Entry(seccion2, bg="#F3F3F3")
NomEn.place(x=150, y=5)
ApePa= Entry(seccion2, bg="#F3F3F3")
ApePa.place(x=200, y=25)
ApeMa= Entry(seccion2, bg="#F3F3F3")
ApeMa.place(x=200, y=45)
Nas= Entry(seccion2, bg="#F3F3F3")
Nas.place(x=220, y=65)
Car= Entry(seccion2, bg="#F3F3F3")
Car.place(x=150, y=85)

ventana.mainloop()