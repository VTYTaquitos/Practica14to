from tkinter import Tk,Button,Frame,messagebox

#creamos una funcion para mostrar un mensaje 
def mostrarMensajes():
    messagebox.showinfo("Aviso", "Presionaste el boton azul")# parametro uno es el titulo de la ventana
    #segundo es el mensaje que viene 
    

#1. Instanciamos el objeto ventana 
ventana = Tk()
ventana.title("Ejemplo de 3 frames") #Titulo de la venta
ventana.geometry("600x400") #Tamaño inicial de la venta

#2. Agregamos los frames
seccion1 = Frame(ventana,bg="black")
seccion1.pack(expand = True, fill = 'both') #la seeccion va agarrar toda la parteque tenga en la ventana


seccion2 = Frame(ventana, bg="red")
seccion2.pack(expand = True, fill = 'both') 

seccion3 = Frame(ventana, bg="yellow")
seccion3.pack(expand = True, fill = 'both') 

#3. Agregamos botones
botonAzul = Button(seccion1,text="Boton azul", fg= "blue",command= mostrarMensajes)
botonAzul.place(x="40",y="60")

#uso del grid
botonAmarrillo = Button(seccion2,text="Boton amarillo", fg= "white", bg="#034B9C")
botonAmarrillo.grid(row= 0,column=0)


botonNegro = Button(seccion2,text="Boton negro", fg= "black", bg="#C6D624")
botonNegro.grid(row= 1,column=3)

#uso del pack
botonVerde = Button(seccion3,text="Boton verde", fg= "#35CD29", bg="#CD29B6")
botonVerde.configure(height=5, width=10) #altura y anchura de un boton
botonVerde.pack()

#Llamamos al main 
ventana.mainloop()