from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import * #Importamos la clase a la ventana

#Creamos un objeto de tipo controlador 
controlador = controladorBD()

#Guardanos usando el metodo de objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(VarNom.get(),VarCorreo.get(),VarContra.get())

#Funcion buscar usuario    
def busquedaUsuario():
    rsUsuario = controlador.consultaUsuario(VarBus.get())
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ usu[1] +" "+usu[2] +" "+ str(usu[3])
    if(rsUsuario):
        texBus.insert('0.0', cadena)
        print(cadena)        
    else:
        messagebox.showinfo("Usuario no encontrado")
        
def MostrarUsuarios():   
    usuarios = controlador.mostrarUsuarios()
    for i in tablaM.get_children():
        tablaM.delete(i)
    for usua in usuarios:
        tablaM.insert("",END,values= (usua[0],usua[1],usua[2]))
        
venatana = Tk()
venatana.title("CRUD Usuarios")
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
titulo = Label(pestana1,text="Registro de usuarios",fg="blue",font= ("Modern",18)).pack()
VarNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre:").pack()
txtNom = Entry(pestana1,textvariable= VarNom).pack()
VarCorreo=tk.StringVar()
lblCorreo=Label(pestana1,text="Correo:").pack()
txtCorreo = Entry(pestana1,textvariable= VarCorreo).pack()
VarContra=tk.StringVar()
lblContra=Label(pestana1,text="Contraseña:").pack()
txtContra = Entry(pestana1,textvariable= VarContra).pack()
btnGuardar = Button(pestana1, text="Guardar",command = ejecutaInsert).pack()

#Pestaña 2 buscar usuario 
titulo = Label(pestana2,text="Buscar usuarios",fg="blue",font= ("Modern",18)).pack()
VarBus=tk.StringVar()
lblid=Label(pestana2,text="Identificador de usuario: ").pack()
txtid = Entry(pestana2,textvariable= VarBus).pack()
btnBusqueda = Button(pestana2, text="Buscar",command=busquedaUsuario).pack()
subBus = Label(pestana2,text="Encontrado",fg="blue",font= ("Modern",14)).pack()
texBus= tk.Text(pestana2,height=5,width=52)
texBus.pack()

#Pestaña 3 
titulo = Label(pestana3,text="Mostrar usuarios",fg="blue",font= ("Modern",18)).pack()
#columnas = ('Id','Nombre','Corr','Contra') 
columnas = ('Id','Nombre','Corr') 
btnMostrar = Button(pestana3, text="Mostrar",command=MostrarUsuarios).pack()
tablaM = ttk.Treeview(pestana3,columns= columnas,show="headings")
tablaM.column("Id", width=100)
tablaM.column("Nombre", width=100)
tablaM.column("Corr", width=100)
#tablaM.column("Contra", width=100)
tablaM.heading("Id",text="ID")
tablaM.heading("Nombre",text="NOMBRE")
tablaM.heading("Corr",text="CORREO")
#tablaM.heading("Contra",text="CONTRASEÑA")
tablaM.pack()

#Texto de las pestañas con su add
panel.add(pestana1,text="Formulario de usuarios")
panel.add(pestana2,text="Buscar usarios")
panel.add(pestana3,text="Consultar usuarios")
panel.add(pestana4,text="Actualizar de usuarios")


venatana.mainloop()