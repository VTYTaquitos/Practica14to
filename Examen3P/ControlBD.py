from tkinter import messagebox
import sqlite3

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C:/Users/frank/OneDrive/Documents/GitHub/Practica14to/Examen3P/BD_Banco.db")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def InsertarBD(self,cue,sal):
        conx = self.conexionBD()
    
        if (cue =="" or sal==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (cue,sal)
            qrInster = "insert into TBCuentas (NoCuenta,Saldo) values (?,?)" 
            cursor.execute(qrInster,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah insertado correctamente el usuario")
    
    
    def CambiarInfo(self,idE,cueE,salE):
        conx = self.conexionBD()
        if (idE == "" or cueE =="" or salE==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (cueE,salE,idE)
            qrActualizar = ("UPDATE TBCuentas SET NoCuenta = ?, Saldo = ? WHERE Id_Cuneta = ?")
            cursor.execute(qrActualizar,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah modificado correctamente el usuario")
            
    def mostrarUsuarios(self):
        conx = self.conexionBD()
        try:
             cursor=conx.cursor()
             sqlMostrar = "select * from TBCuentas"
             cursor.execute(sqlMostrar)
             MResu=cursor.fetchall()
             conx.close()
             return MResu
        except sqlite3.OperationalError:
                print("Error de consulta")