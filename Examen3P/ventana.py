from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ControlBD import *

labasedatos = controladorBD()

def Instertar():
    labasedatos.InsertarBD(VarNom.get(),VarCuenta.get(),VarContra.get())

def ModificarUsuario():        
    labasedatos.CambiarInfo(VarIDC.get(),VarNomC.get(),VarCuentaC.get(),VarContraC.get())

def MostrarUsuarios():   
    usuarios = labasedatos.mostrarUsuarios()
    for i in tablaM.get_children():
        tablaM.delete(i)
    for usua in usuarios:
        tablaM.insert("",END,values= (usua[0],usua[1],usua[2]))
    
venatana = Tk()
venatana.title("BD Usuarios")
venatana.geometry("500x400")

panel = ttk.Notebook(venatana)
panel.pack(fill="both",expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)


#Ventana Insertar 
titulo = Label(pestana1,text="Insterar de usuario",fg="blue",font= ("Modern",18)).pack()
VarNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre:").pack()
txtNom = Entry(pestana1,textvariable= VarNom).pack()
VarCuenta=tk.StringVar()
lblCorreo=Label(pestana1,text="No Cuenta:").pack()
txtCorreo = Entry(pestana1,textvariable= VarCuenta).pack()
VarContra=tk.StringVar()
lblContra=Label(pestana1,text="Contraseña:").pack()
txtContra = Entry(pestana1,textvariable= VarContra).pack()
btnGuardar = Button(pestana1, text="Guardar",command= Instertar).pack()

#Actualizar
titulo = Label(pestana2,text="Modificar usuario",fg="blue",font= ("Modern",18)).pack()
VarIDC=tk.StringVar()
lblIDC=Label(pestana2,text="Id:").pack()
txtIDC = Entry(pestana2,textvariable= VarIDC).pack()
VarNomC=tk.StringVar()
lblNomC=Label(pestana2,text="Nombre:").pack()
txtNomC = Entry(pestana2,textvariable= VarNomC).pack()
VarCuentaC=tk.StringVar()
lblCorreoC=Label(pestana2,text="Cuenta:").pack()
txtCorreoC = Entry(pestana2,textvariable= VarCuentaC).pack()
VarContraC=tk.StringVar()
lblContraC=Label(pestana2,text="Contraseña:").pack()
txtContraC = Entry(pestana2,textvariable= VarContraC).pack()
btnMostrar = Button(pestana2, text="Actualizar",command=ModificarUsuario).pack()


#Mostrar Todo
titulo = Label(pestana3,text="Mostrar usuarios",fg="blue",font= ("Modern",18)).pack()
columnas = ('Id','Nombre','Cuenta') 
tablaM = ttk.Treeview(pestana3,columns= columnas,show="headings")
tablaM.column("Id", width=100)
tablaM.column("Nombre", width=100)
tablaM.column("Cuenta", width=100)
tablaM.heading("Id",text="ID")
tablaM.heading("Nombre",text="NOMBRE")
tablaM.heading("Cuenta",text="NOCUENTA")
tablaM.pack()
btnMostrar = Button(pestana3, text="Mostrar",command=MostrarUsuarios).pack()

panel.add(pestana1,text="Insertar Usuario")
panel.add(pestana2,text="Actualizar Usuario")
panel.add(pestana3,text="Consultar usaurios")



venatana.mainloop()