from tkinter import *
from tkinter import messagebox, ttk
from usuario import usuario

def inicio():
    correo_U = CorreoCa.get()
    contra_U = ContraseñaCa.get()
    admin.Bien(contra_U, correo_U)
    
admin = usuario()
    
#Colocamos la ventana
ventana= Tk()  
ventana.geometry("600x400")
ventana.title("Login de usuario")

seccion1= Frame(ventana,bg= "black")
seccion1.pack(expand=True,fill='both')
 
seccion2= Frame(ventana,bg= "black")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana, bg="black")
seccion3.pack(expand=True,fill='both')

# texto de correo y contraseña 
txtinicio= Label(seccion1,text="Inicio de sesion",bg= "black", fg="orange")
txtinicio.configure(font=("arial", 14))
txtinicio.place(width="650", height="80")

txtCorreo= Label(seccion2,text="Correo:",bg= "black", fg="orange")
txtCorreo.configure(font=("arial",10))
txtCorreo.place(x=90,y=40)

txtContra= Label(seccion2,text="Contraseña:",bg= "black", fg="orange")
txtContra.configure(font=("arial",10))
txtContra.place(x=300,y=40)

# boton
botonIngresar = Button(seccion3,text="Ingresar", fg= "black", bg="orange", command=inicio)
botonIngresar.place(x=90, y=40)

# Colocamos los campos
CorreoCa= Entry(seccion2, bg="#F3F3F3")
CorreoCa.place(x=150, y=43)

ContraseñaCa= Entry(seccion2, bg="#F3F3F3")
ContraseñaCa.place(x=396, y=43)
ContraseñaCa.configure(show="*")
print(ContraseñaCa)

ventana.mainloop()