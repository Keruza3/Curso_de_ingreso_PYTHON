import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Juan Ignacio
apellido: Ullua
---
Ejercicio: while_05
---
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas). 
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        
        letra_ingresada_mayuscula= prompt("ej 5 while" , "Ingrese una letra")

        letra_ingresada_mayuscula = "U"
        letra_ingresada_mayuscula = "T"
        letra_ingresada_mayuscula = "N"

        while letra_ingresada_mayuscula != "U" or letra_ingresada_mayuscula != "T" or letra_ingresada_mayuscula != "N":
           letra_ingresada_mayuscula = prompt("ej 5 while" , "Ingrese una letra nuevamente")
           letra_ingresada_mayuscula = letra_ingresada_mayuscula.upper()
           
        
        alert("ej 5 while" , "Letra ingresada correctamente")


            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()