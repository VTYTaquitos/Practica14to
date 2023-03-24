from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        #Preparamos la coneccion para usar la BD 
        try: 
            conexion = sqlite3.connect("C:/Users/frank/OneDrive/Documents/GitHub/Practica14to/Tkinter&SQLite/BaseTkinter.db")
            print("Conectado a BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    #Metodo de Insertar usuario a la tabla
    def guardarUsuario(self,nom,cor,con):
        #Llamar la conexion
        conx = self.conexionBD()
        
        #Revisar los paramatros vacio
        if (nom == "" or cor =="" or con==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else:
            
            #prepar los datos y el querySQL    
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom,cor,conH)
            qrInster = "insert into TBResgistrados (Nombre,Correo,Contra) values (?,?,?)"
            
            #Insertar y cerrarr conexion 
            
            cursor.execute(qrInster,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah insertado correctamente el usuario")
            
    def encriptarCon(self,con):
        conPlana = con
        conPlana = conPlana.encode() #Cambia la contraseña a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa