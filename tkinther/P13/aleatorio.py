import random
from tkinter import messagebox

class aleatorio():
    def __init__(self):
        self.longitud = ""
        self.mayusculas = "Yes"
        self.caracter = "Yes"
    
    
    def contraF(self,Long,MayusculasC,CaractersC):
        if (self.mayusculas == MayusculasC and self.caracter == CaractersC):
            MayusculasC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            Minuscuulas = "abcdefghijklmnopqrstuvwxyz"
            CaractersC = "!#$%&/()=?¡¨*[]_:;><°" 
            Long = 8
            base = MayusculasC + CaractersC + Minuscuulas
            
        elif(MayusculasC == "No" and CaractersC == "No"  ):
            messagebox.showerror("Contraseñas", "La contraseña sera muy insegura")
            
            for _ in range(5):
                muestra = random.sample(base, Long)
            contraF ="".join(muestra)
            messagebox.showerror("Contraseñas", contraF)           