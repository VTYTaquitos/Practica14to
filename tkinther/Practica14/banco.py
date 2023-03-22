from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from deposito import *

def depositar():
        ventana_deposito = tk.Toplevel()
        ventana_deposito.title("Deposito de dinero")
        ventana_deposito.geometry("600x400")
        
        ##Secciones ventana depositar
        seccionD1 = Frame (ventana_deposito,bg= "black")
        seccionD1.pack(expand=True,fill='both')
        seccionD2 = Frame (ventana_deposito,bg= "black")
        seccionD2.pack(expand=True,fill='both')
        seccionD3 = Frame (ventana_deposito,bg= "black")
        seccionD3.pack(expand=True,fill='both')
        
        ##Textos ventana depositar
        txtDe= Label(seccionD1,text="Deposito de cuenta",bg= "black", fg="orange")
        txtDe.configure(font=("arial", 14))
        txtDe.place(width="650", height="80")
        txtNoc= Label(seccionD2,text="Numero de cuenta: ",bg= "black", fg="orange")
        txtNoc.configure(font=("arial",10))
        txtNoc.place(x=90,y=40)
        txtTI= Label(seccionD2,text="Total a ingresar: ",bg= "black", fg="orange")
        txtTI.configure(font=("arial",10))
        txtTI.place(x=90,y=80)
        
        ##cuadros ventana deposito
        NoDep= Entry(seccionD2, bg="#F3F3F3")
        NoDep.place(x=220, y=43)
        CanDep= Entry(seccionD2, bg="#F3F3F3")
        CanDep.place(x=200, y=80)

        def depo():
                
             NoCuDep = NoDep.get()
             CanDeDep = int(CanDep.get())
             consultaS.Depo(NoCuDep,CanDeDep)    
        
        ##Botones ventana depositar
        botonDepo = Button(seccionD3,text="Confirmar", fg= "black", bg="orange", command= depo )
        botonDepo.place(x=90, y=40)
        botonDepo = Button(seccionD3,text="regresar", fg= "black", bg="orange", command= ventana_deposito.destroy)
        botonDepo.place(x=180, y=40)
        
def retirar():
        ventana_retiro = tk.Toplevel()
        ventana_retiro.title("Reitro de dinero")
        ventana_retiro.geometry("600x400")
        
        ##Secciones ventana Retirar
        seccionR1 = Frame (ventana_retiro,bg= "black")
        seccionR1.pack(expand=True,fill='both')
        seccionR2 = Frame (ventana_retiro,bg= "black")
        seccionR2.pack(expand=True,fill='both')
        seccionR3 = Frame (ventana_retiro,bg= "black")
        seccionR3.pack(expand=True,fill='both')
        
        ##Textos ventana Retirar
        txtRe= Label(seccionR1,text="Retiro de efectivo",bg= "black", fg="orange")
        txtRe.configure(font=("arial", 14))
        txtRe.place(width="650", height="80")
        txtNoc= Label(seccionR2,text="Numero de cuenta: ",bg= "black", fg="orange")
        txtNoc.configure(font=("arial",10))
        txtNoc.place(x=90,y=40)
        txtNIP= Label(seccionR2,text="Ingresa tu NIP: ",bg= "black", fg="orange")
        txtNIP.configure(font=("arial",10))
        txtNIP.place(x=90,y=80)
        txtTR= Label(seccionR2,text="Total a retirar: ",bg= "black", fg="orange")
        txtTR.configure(font=("arial",10))
        txtTR.place(x=90,y=110)
        
        ##cuadros ventana Retirar
        NoRe= Entry(seccionR2, bg="#F3F3F3")
        NoRe.place(x=220, y=43)
        Retnip= Entry(seccionR2, bg="#F3F3F3")
        Retnip.place(x=200, y=80)
        CanRe= Entry(seccionR2, bg="#F3F3F3")
        CanRe.place(x=200, y=110)
        
        def ret():
          
             NoCuDep = NoRe.get()
             Gnip = Retnip.get()
             CanDeRet = CanRe.get()
             consultaS.Ret(NoCuDep,Gnip,CanDeRet)
             
        
        ##Botones ventana Retirar
        botonDepo = Button(seccionR3,text="Retirar", fg= "black", bg="orange", command= ret)
        botonDepo.place(x=90, y=40)
        botonDepo = Button(seccionR3,text="Regresar", fg= "black", bg="orange", command= ventana_retiro.destroy)
        botonDepo.place(x=180, y=40)
        
def Saldo():
        ventana_saldo = tk.Toplevel()
        ventana_saldo.title("Reitro de dinero")
        ventana_saldo.geometry("600x400")
        
        ##Secciones ventana Retirar
        seccionS1 = Frame (ventana_saldo,bg= "black")
        seccionS1.pack(expand=True,fill='both')
        seccionS2 = Frame (ventana_saldo,bg= "black")
        seccionS2.pack(expand=True,fill='both')
        seccionS3 = Frame (ventana_saldo,bg= "black")
        seccionS3.pack(expand=True,fill='both')
        
        ##Textos ventana Retirar
        txtSe= Label(seccionS1,text="Consultar saldo",bg= "black", fg="orange")
        txtSe.configure(font=("arial", 14))
        txtSe.place(width="650", height="80")
        txtSNoc= Label(seccionS2,text="Numero de cuenta: ",bg= "black", fg="orange")
        txtSNoc.configure(font=("arial",10))
        txtSNoc.place(x=90,y=40)
        txtSNIP= Label(seccionS2,text="Ingresa tu NIP: ",bg= "black", fg="orange")
        txtSNIP.configure(font=("arial",10))
        txtSNIP.place(x=90,y=80)
        
        ##cuadros ventana Retirar
        NoCu= Entry(seccionS2, bg="#F3F3F3")
        NoCu.place(x=220, y=43)
        Connip= Entry(seccionS2, bg="#F3F3F3")
        Connip.place(x=200, y=80)

        def Consultar():
             
            NoCuDep = NoCu.get()  
            Gnip  = Connip.get()
            consultaS.Consu(NoCuDep,Gnip)
        
        ##Botones ventana Retirar
        botonDepo = Button(seccionS3,text="Consultar", fg= "black", bg="orange", command= Consultar)
        botonDepo.place(x=90, y=40)
        botonDepo = Button(seccionS3,text="Regresar", fg= "black", bg="orange", command= ventana_saldo.destroy)
        botonDepo.place(x=180, y=40)        
        
ventana= Tk()  
consultaS = banco()  
ventana.geometry("600x400")
ventana.title("Banco del Frank")

##Secciones
seccion1= Frame(ventana,bg= "black")
seccion1.pack(expand=True,fill='both')
 
seccion2= Frame(ventana,bg= "black")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana, bg="black")
seccion3.pack(expand=True,fill='both')

##Textos
txtinicio= Label(seccion1,text="Bienvenido a FB",bg= "black", fg="orange")
txtinicio.configure(font=("arial", 14))
txtinicio.place(width="650", height="80")

txtinicio= Label(seccion2,text="Indica que accion deseas realizar",bg= "black", fg="orange")
txtinicio.configure(font=("arial", 14))
txtinicio.place(width="650", height="80")

botonDepo = Button(seccion3,text="Depositar", fg= "black", bg="orange", command = depositar )
botonDepo.place(x=90, y=40)

botonRet = Button(seccion3,text="Retirar", fg= "black", bg="orange", command = retirar)
botonRet.place(x= 300, y=40)

botonCon = Button(seccion3,text="Consultar saldo", fg= "black", bg="orange", command = Saldo)
botonCon.place(x= 500, y=40)

ventana.mainloop()