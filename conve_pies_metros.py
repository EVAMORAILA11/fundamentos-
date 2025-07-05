from tkinter import *
from tkinter import ttk

def calcular(*arg):
    try:  #convertir el valor a metros en 2 pasos 
        valor = float(pies.get()) #parcial (es una operacion de tipo de dato)
        metros.set((0.3048 *valor*10000.0+.5)/10000.0) #asigna el valor 
    except ValueError:  
        pass

raiz = Tk()  #objeto raiz ventana
raiz.title("Pies a Metros") #al objeto se le pone titulo

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12") #se crea un marco de trabajo, padding es unatributo que dice cuanto e separa de las orillas 
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))  #Sticky a donde se carga (posicion)
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)


pies = StringVar()
metros = StringVar()

txtPies = ttk.Entry(marcoPrincipal, width=7, textvariable=pies) #se define la caja e texto y el objeto padre(marco principal)
txtPies.grid(column=2, row=1, sticky=(W, E)) #donde se desea poner

ttk.Label(marcoPrincipal, textvariable=metros).grid(column=2, row=3, sticky=W) #etiqueta
ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=3, row=3, sticky=W) #comand llama a la funcion 

ttk.Label(marcoPrincipal, text="pies").grid(column=3, row=1, sticky=W)
ttk.Label(marcoPrincipal, text="es equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(marcoPrincipal, text="metros").grid(column=3, row=2, sticky=W)

for child in marcoPrincipal.winfo_children(): #inicio y fin del contenido 
    child.grid_configure(padx=5, pady=5)

txtPies.focus()
raiz.bind('<Return>', calcular)

raiz.mainloop() #llamar un ciclo para que se ejecute 