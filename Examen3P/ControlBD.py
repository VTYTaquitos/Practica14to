from tkinter import messagebox
import sqlite3

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C:/Users/frank/OneDrive/Documents/GitHub/Practica14to/Examen3P/BD_Banco.db")
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def InsertarBD(self,nom,cue,con):
        conx = self.conexionBD()
    
        if (nom == "" or cue =="" or con==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (nom,cue,con)
            qrInster = "insert into TBCunetas (Nombre,NoCuenta,Contra) values (?,?,?)" 
            cursor.execute(qrInster,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah insertado correctamente el usuario")
    
    
    def CambiarInfo(self,idE,nomE,cueE,conE):
        conx = self.conexionBD()
        if (idE == "" or nomE == "" or cueE =="" or conE==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else:
            cursor = conx.cursor()
            conH = self.encriptarCon(conE)
            #datos = (nomE,corE,conH)
            datos = (nomE,cueE,conH,idE)
            qrActualizar = ("UPDATE TBCunetas SET Nombre = ?, NoCuenta = ?, Contra = ? WHERE Id = ?")
            cursor.execute(qrActualizar,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah modificado correctamente el usuario")
            
    def mostrarUsuarios(self):
        conx = self.conexionBD()
        try:
             cursor=conx.cursor()
             sqlMostrar = "select * from TBCunetas"
             cursor.execute(sqlMostrar)
             MResu=cursor.fetchall()
             conx.close()
             return MResu
        except sqlite3.OperationalError:
                print("Error de consulta")