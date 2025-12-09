import tkinter as tk
from tkinter import ttk
from Datos import calculo_ratios_metricas
from grafico import implementar_grafico

import yfinance as yf


# Colores
FONDO = "#F7F9FC"
BORDE = "#DEE2E6"
GRIS= "#6C757D"
VERDE = "#28A745"
ROJO = "Red"
BLANCO="white"
AZUL="#007BFF"




def obtener_ingresos(Nombre_accion):

    Accion=yf.Ticker(Nombre_accion)
    di = Accion.income_stmt
    ingresos = di.loc["Total Revenue"]
    return ingresos.sort_index(ascending=True)

def obtener_beneficios(Nombre_accion):

    Accion = yf.Ticker(Nombre_accion)

    df = Accion.income_stmt

    beneficios = df.loc["Net Income"]
    return beneficios.sort_index(ascending=True)

def obtener_dividendos(Nombre_accion):
    Accion = yf.Ticker(Nombre_accion)

    div = Accion.dividends
    
    div_año = div.groupby(div.index.year).sum()
    return div_año.sort_index(ascending=True)



def ventana_2(Nombre_accion):
    datos=calculo_ratios_metricas(Nombre_accion)
    ventana2=tk.Tk()
    ventana2.geometry("750x500")
    ventana2.title("Detalle de la Acción")
    ventana2.configure(bg=FONDO)

    estilo=ttk.Style()
    estilo.theme_use("clam")

    contenedor = tk.Frame(ventana2,bg=FONDO,padx=20,pady=20,height=100)
    contenedor.pack(fill="both",expand=1)
    contenedor.pack_propagate(False)

    detalles=tk.Frame(contenedor,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0,relief="flat",height=100)
    detalles.pack(fill="both", expand=True, padx=20, pady=20)

    marco_sup= tk.Frame(detalles,bg="white")
    marco_sup.pack(fill="x",padx=20,pady=(15,5))

    comp=tk.Frame(marco_sup,bg="white")
    comp.pack(side="left",fill="y")

    #Siglas de la empresa(prueba con apple):AAPL 
    tk.Label(comp,text=Nombre_accion,font=("Arial",16,"bold",),bg="white",fg="black").pack(side="left",padx=(0,5))

    #sector de la empresa
    sector= tk.Label(comp,text=datos[1],font=("Arial",10),bg=FONDO,fg=GRIS,padx=8,pady=2,relief="flat")
    sector.pack(side="left",fill="y")

    #precio actual
    precio= tk.Frame(marco_sup,bg="white")
    precio.pack(side='right', fill='y')

    tk.Label(precio,text=datos[2],font=("Arial", 28), bg="white",fg="black").pack(anchor="e")
    #porcentaje de cambio
    tk.Label(precio,text=f"{datos[3]:.2f}%",font=("Arial", 14),bg="white",fg=f"{VERDE if datos[3]>0 else ROJO}").pack(anchor='e')

    #nombre de la empresa prueba apple
    tk.Label(detalles,text=datos[0],font=("Arial", 14), bg="white", fg='black',anchor='w').pack(fill='x', padx=20, pady=(0, 10))

    tk.Label(detalles,text=f"{datos[4] if None else datos[5]}",font=("Arial", 11),bg="white",justify='left',wraplength=500,anchor='w').pack(fill='x', padx=20, pady=(0, 15))

    tk.Label(detalles,text="Hoy",font=("Arial", 10), bg="white",fg=GRIS,anchor='e').pack(fill='x', padx=20, pady=(0, 15))

    #resto de datos zzzzz

    #1 zdasdasdas
    zzz= tk.Frame(contenedor,bg=FONDO,padx=20,pady=10)
    zzz.pack(fill='x') 

    zzz1=tk.Frame(zzz,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0, relief="flat",width=175,height=75)
    zzz1.pack(side="left",padx=(0,15),fill="y")
    zzz1.pack_propagate(False)

    tk.Label(zzz1,text="Ingresos", font=("Arial", 9),bg="white",fg=GRIS, anchor="w").pack(fill="x",padx=10,pady=5)

    inf=tk.Frame(zzz1,bg="white")
    inf.pack(fill='x', padx=10)

    tk.Label(inf,text=datos[6],font=("Arial", 14, "bold"),bg="white" ,fg="black",anchor="w").pack(side='left')

    #2
    zzz2=tk.Frame(zzz,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0, relief="flat",width=100,height=75)
    zzz2.pack(side="left",padx=(0,15),fill="y")
    zzz2.pack_propagate(False)

    tk.Label(zzz2, text="P/E - ratio", font=("Arial", 9),bg="white",fg=GRIS, anchor="w").pack(fill="x",padx=10,pady=5)

    inf2=tk.Frame(zzz2,bg="white")
    inf2.pack(fill='x', padx=10)

    tk.Label(inf2,text=f"{datos[7]:.2f}",font=("Arial", 14, "bold"),bg="white" ,fg="black",anchor="w").pack(side='left')

    #3
    zzz3=tk.Frame(zzz,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0, relief="flat",width=100,height=75)
    zzz3.pack(side="left",padx=(0,15),fill="y")
    zzz3.pack_propagate(False)

    tk.Label(zzz3, text="P/B - ratio", font=("Arial", 9),bg="white",fg=GRIS, anchor="w").pack(fill="x",padx=10,pady=5)

    inf3=tk.Frame(zzz3,bg="white")
    inf3.pack(fill='x', padx=10)

    tk.Label(inf3,text=f"{datos[8]:.2f}",font=("Arial", 14, "bold"),bg="white" ,fg="black",anchor="w").pack(side='left')
    #4
    zzz4=tk.Frame(zzz,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0, relief="flat",width=100,height=75)
    zzz4.pack(side="left",padx=(0,15),fill="y")
    zzz4.pack_propagate(False)

    tk.Label(zzz4, text="Dividen yield", font=("Arial", 9),bg="white",fg=GRIS, anchor="w").pack(fill="x",padx=10,pady=5)

    inf4=tk.Frame(zzz4,bg="white")
    inf4.pack(fill='x', padx=10)

    tk.Label(inf4,text=f"{datos[9]:.2f}%",font=("Arial", 14, "bold"),bg="white" ,fg="black",anchor="w").pack(side='left')

    #5
    zzz5=tk.Frame(zzz,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0, relief="flat",width=150,height=75)
    zzz5.pack(side="left",fill="y")
    tk.Label(zzz5, text="Margen de beneficio", font=("Arial", 9),bg="white",fg=GRIS, anchor="w").pack(fill="x",padx=10,pady=5)

    inf5=tk.Frame(zzz5,bg="white")
    inf5.pack(fill='x', padx=10)

    tk.Label(inf5,text=f"{datos[10]:.2f} %",font=("Arial", 14, "bold"),bg="white" ,fg="black",anchor="w").pack(side='left')


    #grafico
    def mostrar_ingresos():
        dia_d=obtener_ingresos(Nombre_accion)
        implementar_grafico(dia_d,"Ingresos Anuales", "Total Ingreso")

    def mostrar_beneficios():
        ancson = obtener_beneficios(Nombre_accion)
        implementar_grafico(ancson, "Beneficio Neto Anual", "Ingreso Neto")
    
    def mostrar_dividendos():
        cnuicizuxc = obtener_dividendos(Nombre_accion)
        implementar_grafico(cnuicizuxc, "Dividendos por Año", "Dividendos")


    grafico= tk.Frame(contenedor,bg="white",highlightbackground=BORDE,highlightthickness=1,bd=0,relief="flat")
    grafico.pack(fill='both', expand=True, padx=20, pady="15")

    #botones graf

    botones = tk.Frame(grafico, bg="white", padx=10, pady=10)
    botones.pack(fill="both", expand=True)

    asdpo=tk.Frame(grafico,bg="white")
    asdpo.pack(fill="both", expand=True)

    boton1 = ttk.Button(botones, text="Ingresos Anuales", command=mostrar_ingresos)
    boton1.pack(side="left", padx=5)

    boton2 = ttk.Button(botones, text="Beneficios Anuales", command=mostrar_beneficios)
    boton2.pack(side="left", padx=5)

    boton3 = ttk.Button(botones, text="Dividendos Anuales", command=mostrar_dividendos)
    boton3.pack(side="left", padx=5)

    mostrar_ingresos()

    ventana2.mainloop()

    
   