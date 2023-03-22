import random
from tkinter import messagebox
from tkinter import *

class matricula():
    def __init__(self):
        pass
    def Crear(self, nombre, paterno, materno, nacimiento, carrera):
        self.NombreE = nombre 
        self.ApePapa = paterno 
        self.ApeMama = materno
        self.AñoNas = nacimiento 
        self.CarreraE = carrera
        curso = str(2023)
        
        losrandom = random.randint(100,200)
        numeros = str(losrandom)
        
        orden = carrera[:3] + curso[-2:] + nacimiento[-2:] + nombre[:1] + paterno[:3] + materno[:3] + numeros
        
        messagebox.showinfo("Matricula","La matricula es: "+ orden)