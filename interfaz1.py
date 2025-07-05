from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

# Ventana principal
raiz = Tk()
raiz.title("Muestra Widgets")


# Variables
nombre = StringVar()
apaterno = StringVar()
amaterno = StringVar()
correo = StringVar()
movil = StringVar()
estado = StringVar()
ocupacion = StringVar()
leer = BooleanVar()
musica = BooleanVar()
videojuegos = BooleanVar()

# Lista de estados
estados = [
    "Estados(32)", "Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
    "Chiapas", "Chihuahua", "CDMX", "Coahuila", "Colima", "Durango",
    "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán",
    "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro",
    "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco",
    "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
]

# Guardar datos 
def guardar():
    nom = nombre.get()
    pat = apaterno.get()
    mat = amaterno.get()
    mail = correo.get()
    tel = movil.get()
    edo = estado.get()
    ocup = ocupacion.get()

    aficiones = []
    if leer.get():
        aficiones.append('Leer')
    if musica.get():
        aficiones.append('Música')
    if videojuegos.get():
        aficiones.append('Videojuegos')
    
  
    with open('informacion.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nom, pat, mat, mail, tel, ocup, ', '.join(aficiones), edo])

    messagebox.showinfo("Guardado", "Los datos fueron guardados correctamente.")
    limpiar()

# Limpiar
def limpiar():
    nombre.set("")
    apaterno.set("")
    amaterno.set("")
    correo.set("")
    movil.set("")
    estado.set("")
    ocupacion.set("")
    leer.set(False)
    musica.set(False)
    videojuegos.set(False)
    comboEstado.current(0)

# Marco principal 
marcoPrincipal = ttk.Frame(raiz, padding="5 5 20 20")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
raiz.columnconfigure(0, weight=1)
raiz.rowconfigure(0, weight=1)

# Entradas y etiquetas
frame_datos = ttk.LabelFrame(marcoPrincipal, text="Datos Personales", padding="10 10 10 10")
frame_datos.grid(column=0, row=0, columnspan=3, padx=10, pady=10, sticky=(W, E))

ttk.Label(marcoPrincipal, text="Nombre:").grid(column=1, row=1, sticky=W)
entry_nombre = ttk.Entry(marcoPrincipal, width=30, textvariable=nombre)
entry_nombre.grid(column=2, row=1, sticky=(W, E))

ttk.Label(marcoPrincipal, text="A.paterno:").grid(column=1, row=2, sticky=W)
entry_apaterno = ttk.Entry(marcoPrincipal, width=30, textvariable=apaterno)
entry_apaterno.grid(column=2, row=2, sticky=(W, E))

ttk.Label(marcoPrincipal, text="A.materno:").grid(column=1, row=3, sticky=W)
entry_amaterno = ttk.Entry(marcoPrincipal, width=30, textvariable=amaterno)
entry_amaterno.grid(column=2, row=3, sticky=(W, E))

ttk.Label(marcoPrincipal, text="Correo:").grid(column=1, row=4, sticky=W)
entry_correo = ttk.Entry(marcoPrincipal, width=30, textvariable=correo)
entry_correo.grid(column=2, row=4, sticky=(W, E))

ttk.Label(marcoPrincipal, text="Movil:").grid(column=1, row=5, sticky=W)
entry_movil = ttk.Entry(marcoPrincipal, width=30, textvariable=movil)
entry_movil.grid(column=2, row=5, sticky=(W, E))

# Combobox
comboEstado = ttk.Combobox(marcoPrincipal, textvariable=estado, values=estados, width=27)
comboEstado.grid(column=4, row=7, sticky=W)
comboEstado.current(0)

# Button
#Frame  principal 
frame_botones = Frame(marcoPrincipal)
frame_botones.grid(column=1 , row=10, columnspan=2, pady=10)

ttk.Button(frame_botones, text="Guardar", command=guardar).grid(column=0, row=0, padx=10)
ttk.Button(frame_botones, text="Cancelar", command=limpiar).grid(column=1, row=0, padx=10)

#Radiobutton 
#Frame principal
frame_ocupacion = Frame(marcoPrincipal)
frame_ocupacion.grid(column=4, row=3, sticky=W)

Radiobutton(frame_ocupacion, text="Estudiante", variable=ocupacion, value="Estudiante").grid(row=0, column=5, sticky=W)
Radiobutton(frame_ocupacion, text="Empleado", variable=ocupacion, value="Empleado").grid(row=1, column=5, sticky=W)
Radiobutton(frame_ocupacion, text="Desempleado", variable=ocupacion, value="Desempleado").grid(row=2, column=5, sticky=W)

 
# Checkbutton
frame_aficiones_estado = Frame(marcoPrincipal)
frame_aficiones_estado.grid(column=1, row=7, columnspan=2, sticky=W)

frame_aficiones = LabelFrame(frame_aficiones_estado, padx=10, pady=10)
frame_aficiones.grid(row=0, column=0, padx=5)

Checkbutton(frame_aficiones, text="Leer", variable=leer).grid(row=0, column=0, sticky=W)
Checkbutton(frame_aficiones, text="Música", variable=musica).grid(row=0, column=1, sticky=W)
Checkbutton(frame_aficiones, text="Videojuegos", variable=videojuegos).grid(row=0, column=2, sticky=W)
 
# Padding
for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=6, pady=6)

entry_nombre.focus()
raiz.mainloop()
