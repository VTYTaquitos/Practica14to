from tkinter import *
from tkinter import ttk
import tkinter as tk
from LoginClass import * #Importamos la clase a la ventana

#Creamos un objeto de tipo controlador 
controlador = controladorBD()

#Guardanos usando el metodo de objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(VarRENom.get(),VarRECorreo.get(),VarREContra.get(),VarRENick.get())

venatana = Tk()
venatana.title("BestPlay Simulator")
venatana.geometry("500x400")

#Panel
panel = ttk.Notebook(venatana)
panel.pack(fill="both",expand="yes")

#Pestañas
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)


#Pestaña1 Formulario
titulo = Label(pestana1,text="Inicio de sesion",fg="white",bg="black",font= ("Modern",18)).pack()
VarCorreo=tk.StringVar()
lblCorreo=Label(pestana1,text="Correo:",fg="white",bg="black").pack()
txtCorreo = Entry(pestana1,textvariable= VarCorreo).pack()
VarContra=tk.StringVar()
lblContra=Label(pestana1,text="Contraseña:",fg="white",bg="black").pack()
txtContra = Entry(pestana1,textvariable= VarContra).pack()

#Pestaña2 Formulario
titulo = Label(pestana2,text="Registro de usuarios",fg="blue",font= ("Modern",18)).pack()
VarRENom=tk.StringVar()
lblNom=Label(pestana2,text="Nombre:",fg="white",bg="black").pack()
txtNom = Entry(pestana2,textvariable= VarRENom).pack()
VarRECorreo=tk.StringVar()
lblCorreo=Label(pestana2,text="Correo:",fg="white",bg="black").pack()
txtCorreo = Entry(pestana2,textvariable= VarRECorreo).pack()
VarREContra=tk.StringVar()
lblContra=Label(pestana2,text="Contraseña:",fg="white",bg="black").pack()
txtContra = Entry(pestana2,textvariable= VarREContra).pack()
VarRENick=tk.StringVar()
lblNick=Label(pestana2,text="Nickname:",fg="white",bg="black").pack()
txtNick = Entry(pestana2,textvariable= VarRENick).pack()
btnGuardar = Button(pestana2, text="Guardar",command = ejecutaInsert).pack()

#Texto de las pestañas con su add
panel.add(pestana1,text="Inicio de sesion")
panel.add(pestana2,text="Registro de Usuario")


venatana.mainloop()