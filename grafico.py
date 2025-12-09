import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

BLANCO="white"
AZUL="#007BFF"

canvas_actual = None 
frame_grafico = None

def implementar_grafico(datos, titulo, ylabel):
    global canvas_actual
    global frame_grafico

    if canvas_actual is not None:
        canvas_actual.get_tk_widget().destroy()
        plt.close('all') 
        canvas_actual = None

    
    fig, ax = plt.subplots(figsize=(1, 1))

    if hasattr(datos.index, "year"):
        x = datos.index.year
    else:
        x = datos.index
    

    if "Total Ingreso" in ylabel or "Ingreso Neto" in ylabel:
        valores_y = datos.values / 1e9
        ylabel += " (Billones USD)"
    else:
        valores_y = datos.values



    ax.plot(x, valores_y, marker="o", color=AZUL)
    ax.set_title(titulo, fontsize=12, loc='left', color='#343A40')
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_xlabel("Año", fontsize=9)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    

    ax.set_xticks(x)
    ax.set_xticklabels([str(a) for a in x], rotation=45, ha='right')

    fig.patch.set_facecolor(BLANCO) 
    ax.set_facecolor(BLANCO) 
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10) 
    canvas.draw()

    canvas_actual = canvas