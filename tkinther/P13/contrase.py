from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from aleatorio import aleatorio
              
def generar():
    longitud = Long.get()
    #mayusculas = MayuDrop.get()
    mayusculas = MayuDrop.get()
    #caracter = CaraDrop.get() 
    caracter = CaraDrop.get() 
    contra.contraF(longitud, mayusculas, caracter)   
               
contra = aleatorio()       
    
ventana= Tk()  
ventana.geometry("600x400")
ventana.title("Generador de contraseñas")

##Secciones
seccion1= Frame(ventana,bg= "black")
seccion1.pack(expand=True,fill='both')
 
seccion2= Frame(ventana,bg= "black")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana, bg="black")
seccion3.pack(expand=True,fill='both')

##Textos
txtinicio= Label(seccion1,text="Generador de contraseñas",bg= "black", fg="orange")
txtinicio.configure(font=("arial", 14))
txtinicio.place(width="650", height="80")

txtLon= Label(seccion2,text="Longitud: ",bg= "black", fg="orange")
txtLon.configure(font=("arial",10))
txtLon.place(x=90,y=40)

txtMayu= Label(seccion2,text="Mayusculas: ",bg= "black", fg="orange")
txtMayu.configure(font=("arial",10))
txtMayu.place(x=90,y=80)

txtCar= Label(seccion2,text="Caracteres: ",bg= "black", fg="orange")
txtCar.configure(font=("arial",10))
txtCar.place(x=90,y=110)

#campos de interaccion 
Long= Entry(seccion2, bg="#F3F3F3")
Long.place(x=150, y=43)

mayusculas = StringVar()
MenuMayu = [
    'Yes',
    'No'
]
mayusculas.set(MenuMayu[0])
MayuDrop = OptionMenu (seccion2,mayusculas, *MenuMayu)
MayuDrop.place(x=170, y=73)

caracteres = StringVar()
MenuCara = [
    'Yes',
    'No'
]
mayusculas.set(MenuCara[0])
CaraDrop = OptionMenu (seccion2,mayusculas, *MenuCara)
CaraDrop.place(x=170, y=100)
"""MayuDrop= Entry(seccion2, bg="#F3F3F3")
MayuDrop.place(x=170, y=80)

CaraDrop= Entry(seccion2, bg="#F3F3F3")
CaraDrop.place(x=170, y=110)"""

##Boton
botonGenerar = Button(seccion3,text="Generar", fg= "black", bg="orange",command=generar)
botonGenerar.place(x=90, y=40)

ventana.mainloop()