import tkinter as tk
from tkinter import ttk
from interfas2 import ventana_2

ventana= tk.Tk()
ventana.geometry("1000x850")
# ventana.configure(bg="white")
ventana.title("Bolsa de Valores")

busqueda = tk.Entry(font=("Arial",12))
busqueda.pack(pady=30)



def Obtener_Accion():
    Nombre_accion=busqueda.get()
    ventana_2(Nombre_accion)


boton = tk.Button(ventana,text="Buscar Acción", command=Obtener_Accion)
boton.pack()

ventana.mainloop()