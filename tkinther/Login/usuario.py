from tkinter import messagebox, ttk
class usuario():
    def __init__(self) -> None:
        self.correo_U ="flujan@gmail.com"
        self.contra_U ="1234"
    def Bien(self,contrase,correo):
        if(self.contra_U == contrase and self.correo_U == correo):
         messagebox.showerror("Bienvenido", "bien")
        elif(contrase == "" and correo == ""):
            messagebox.showerror("Error", "Esta vacio")
        else:
             messagebox.showerror("Error", "Ta mal")
        