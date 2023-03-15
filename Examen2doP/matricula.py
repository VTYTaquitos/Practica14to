import random
from tkinter import messagebox
from tkinter import *

class matricula():
    def __init__(self):
        self.Nombre_E = ""
        self.ApePapa = ""
        self.ApeMama = ""
        self.AñoNas = ""
        self.Carrera_E = ""
    
    def Crear(self, nombre, paterno, materno, nacimiento, carrera):
        
        nombre =  self.Nombre_E
        paterno = self.ApePapa
        materno = self.ApeMama
        nacimiento = self.AñoNas
        carrera =  self.Carrera_E
        datos = nombre + paterno + materno + nacimiento + carrera
        curso = 2023
        
        muestra = random.sample(datos,curso)
        messagebox.showerror("Matricula","La matricula es: " + muestra)  