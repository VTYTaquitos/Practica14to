import random
from tkinter import messagebox
from tkinter import *

class matricula():
    def __init__(self):
        self.NombreE = ""
        self.ApePapa = ""
        self.ApeMama = ""
        self.AñoNas = ""
        self.CarreraE = ""
    
    def Crear(self, nombre, paterno, materno, nacimiento, carrera):
        
        nombre =  self.NombreE
        paterno = self.ApePapa
        materno = self.ApeMama
        nacimiento = self.AñoNas
        carrera =  self.CarreraE
        curso =str(2023)
        orden = carrera + curso + nacimiento + nombre + paterno + materno
        
        messagebox.showinfo("Matricula","La matricula es: "+ orden)