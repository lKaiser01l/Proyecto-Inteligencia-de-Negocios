import tkinter as tk
from tkinter import ttk
from interfas2 import ventana_2


def main():
    ventana= tk.Tk()
    ventana.geometry("1000x850")
    # ventana.configure(bg="white")
    ventana.title("Bolsa de Valores")

    tickers=["AAPL", "GOOGL", "MSFT", "TSLA"]

    selecion= tk.StringVar()
    busqueda = ttk.Combobox(ventana,textvariable=selecion, values=tickers,font=("Arial",12),width=30)

    busqueda.pack(pady=30)



    def Obtener_Accion():
        Nombre_accion=busqueda.get()
        ventana_2(Nombre_accion)


    boton = tk.Button(ventana,text="Buscar Acción", bg="white",bd=0,command=Obtener_Accion)
    boton.pack()

    ventana.mainloop()


if __name__ == "__main__":
    main()
