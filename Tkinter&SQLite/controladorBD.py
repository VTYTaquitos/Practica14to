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
        return conHa
    
    def consultaUsuario(self,id):
        conx = self.conexionBD()
        if(id == ""):#si el ID esta vacio
         messagebox.showwarning("Ojo","Pon algo capo")
         conx.close()
        else: #buscar el ID 
            try:
                cursor=conx.cursor() #llamamos la conexion
                sqlSelect = "select * from TBResgistrados where Id="+ id #enviamos la consulta
                cursor.execute(sqlSelect)#Ejecucion del guardado de la consulta
                RSusuario = cursor.fetchall() 
                conx.close() #cerramos la conexion
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error de consulta1")
    
    def mostrarUsuarios(self):
        conx = self.conexionBD()
        try:
             cursor=conx.cursor()
             sqlMostrar = "select * from TBResgistrados"
             cursor.execute(sqlMostrar)
             MResu=cursor.fetchall()
             conx.close()
             return MResu
        except sqlite3.OperationalError:
                print("Error de consulta")

    def edicionUsuario(self,idE,nomE,corE,conE):
        conx = self.conexionBD()
        if (idE == "" or nomE == "" or corE =="" or conE==""):
            messagebox.showwarning("Cuidado","Revisa lo que pusiste")
            conx.close()
        else:
            cursor = conx.cursor()
            conH = self.encriptarCon(conE)
            #datos = (nomE,corE,conH)
            datos = (nomE,corE,conH,idE)
            qrActualizar = ("UPDATE TBResgistrados SET Nombre = ?, Correo = ?, Contra = ? WHERE Id = ?")
            cursor.execute(qrActualizar,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Bien","Se ah modificado correctamente el usuario")
    
    def eliminarUsuarioBD(self,idEE):
        conx = self.conexionBD()  
        try:
            cursor = conx.cursor()
            qrEliminar = ("DELETE FROM TBResgistrados WHERE Id = ?")
            datos = (idEE)
            confi = messagebox.askokcancel("Confirmacion","Esta seguro de querer eliminar esta info")
            if confi == True:
                cursor.execute(qrEliminar,datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Elimino","Se a eliminado el perfil")
            else:
                conx.close()
                messagebox.showinfo("Error","No se pudo completar la accion")
        except sqlite3.OperationalError:
                print("Error de consulta")
