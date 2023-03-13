import random
from tkinter import messagebox
from tkinter import *
class banco():
    
    def __init__(self) -> None:
        self.NoCuDep ="4250"
        self.CanDeDep =""
        self.Gnip = "3411"
        self.CanDeRet = ""
        self.saldoT = 500
        
    def Depo(self,nocuenta,deposito):
        if(self.NoCuDep == nocuenta):
         messagebox.showerror("Bienvenido", "Has depositado: " + str(deposito))
         self.saldoT += deposito
         print(str(self.saldoT))
        else:
             messagebox.showerror("Error", "Ta mal")
     
    def Ret(self, nocuenta, nip, retiro):
        if(self.NoCuDep == nocuenta and self.Gnip == nip):
            messagebox.showerror("Retiro exitoso", "Favor de tomar tu efectivo: " +str(retiro))
            self.saldoT -= retiro
        else:
            messagebox.showerror("Retiro fallido", "Consulta tu saldo o revisa que los datos esten bien")
    
    def Consu(self, nocuenta, nip):
        if(self.NoCuDep ==  nocuenta and self.Gnip == nip):
            #saldoActual = self.saldoT
            messagebox.showerror("Consulta de saldo","Tu saldo actual es: " + str(self.saldoT))
        else:
            messagebox.showerror("Consulta de saldo", "Datos incorrectos")