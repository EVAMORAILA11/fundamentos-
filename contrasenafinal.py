from tkinter import *
from tkinter import ttk

#inicio la ventan es el objeto raiz 
raiz = Tk()
raiz.title("Inicio Sesión")

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)

usuario = StringVar()
contrasena=StringVar()


#caja de texto 
txtusuario = ttk.Entry(marcoPrincipal, width=7, textvariable=usuario)
txtusuario.grid(column=2, row=1, sticky=(W, E))
txtcontrasena = ttk.Entry(marcoPrincipal, width=7, textvariable=usuario)
txtcontrasena.grid(column=2, row=2, sticky=(W, E))

#Boton 
ttk.Label(marcoPrincipal, textvariable=contrasena).grid(column=2, row=3, sticky=W)
ttk.Button(marcoPrincipal, text="Ingresar").grid(column=3, row=3, sticky=W)

#Etiqueta 
ttk.Label(marcoPrincipal, text="Usuario").grid(column=1, row=1, sticky=W)
ttk.Label(marcoPrincipal, text="Contraseña").grid(column=1, row=2, sticky=E)

# Distancia de widgest
for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

txtusuario.focus()

raiz.mainloop()
