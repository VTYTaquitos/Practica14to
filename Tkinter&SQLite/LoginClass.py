from tkinter import messagebox
import sqlite3
import bcrypt


class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C:/Users/frank/OneDrive/Documents/GitHub/Practica14to/Tkinter&SQLite/BaseTkinter.db")
            print("Conectado a BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
   
    def guardarUsuario(self,nom,cor,con,nick):
        conx = self.conexionBD()
        if (nom == "" or cor =="" or con=="" or nick ==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else: 
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom,cor,conH,nick)
            qrInster = "insert into BetsPlay (Nombre,Correo,Contrase,Nickname) values (?,?,?,?)"
            
            cursor.execute(qrInster,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah guardado correctamente el usuario")
            
            
    def encriptarCon(self,con):
        conPlana = con
        conPlana = conPlana.encode() #Cambia la contraseña a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa         