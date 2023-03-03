from tkinter import Tk,Button,Frame,messagebox,Label,Entry

Correo_perfil= "franklujan@gmail.com"
contra_perfil= "taquero34"

# Hacemos la verificacion del correo y contraseña 
def Verificacion():
    if contra_perfil == ContraseñaCa.get() and Correo_perfil == CorreoCa.get():
        messagebox.showerror("Acceso permitido","Iniciaste sesion correctamente")
    else:
        messagebox.showerror("Error de inicio de sesion ","verifique correo o contraseña")


#1. Colocamos la ventana
ventana= Tk()   
ventana.geometry("600x400")
ventana.title("Login")

seccion1= Frame(ventana)
seccion1.pack(expand=True,fill='both')
 
seccion2= Frame(ventana)
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana)
seccion3.pack(expand=True,fill='both')

#texto de correo y contraseña 
txtinicio= Label(seccion1,text="Inicio de sesion")
txtinicio.configure(font=("arial", 14))
txtinicio.place(width="650", height="80")

txtCorreo= Label(seccion2,text="Correo:",fg="black")
txtCorreo.configure(font=("arial",10))
txtCorreo.place(x=90,y=40)

txtContra= Label(seccion2,text="Contraseña:",fg="black")
txtContra.configure(font=("arial",10))
txtContra.place(x=300,y=40)

# colocamos los campos
CorreoCa= Entry(seccion2, bg="#F3F3F3")
CorreoCa.place(x=150, y=43)

ContraseñaCa= Entry(seccion2, bg="#F3F3F3")
ContraseñaCa.place(x=396, y=43)
ContraseñaCa.configure(show="*")
print(ContraseñaCa)


#3. agregamos los botones

btonloG= Button(seccion3,text="INGRESAR",fg="black",bg="white",command=Verificacion)
btonloG.configure(height=2,width=10)
btonloG.pack()

ventana.mainloop()