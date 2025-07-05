from tkinter import *  
from tkinter import ttk

# raiz
raiz = Tk()

boton = ttk.Label(raiz, text="Etiqueta solo texto")
boton.grid()

# imagen 
imagen = PhotoImage(file="C:\\Users\\evapl\\Desktop\\Interfaz\\flor.png")

botImagen = ttk.Label(raiz, image=imagen)
botImagen.grid()

botCombinado = ttk.Button(raiz, text="Etiqueta combinada", image=imagen, compound="bottom")
botCombinado.grid()

raiz.mainloop()
