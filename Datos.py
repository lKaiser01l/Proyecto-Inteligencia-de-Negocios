import yfinance as yf


def calculo_ratios_metricas(Nombre_Accion):
    #Base

    Accion= yf.Ticker(Nombre_Accion)
    nombre_empresa = Accion.info.get("longName")
    sector=Accion.info.get("sector")

    descripcion = Accion.info.get("shortBusinessSummary")
    descripcion2= Accion.info.get("longBusinessSummary")

    #graf
    grafico_ingresos_anuales= Accion.financials.loc["Total Revenue"]


    res_2= descripcion2[:125]+ "..."

    Costo_Accion=Accion.info["regularMarketPrice"]
    ingresos= Accion.financials.loc["Total Revenue"].iloc[0]

    #porcentaje de variacion
    precio_actual =Accion.fast_info["last_price"]
    precio_anterior = Accion.fast_info["previous_close"]
    porcentaje = ((precio_actual-precio_anterior)/precio_anterior)*100

    #Calculos
    #P/E => costo Accion/eps
    eps=Accion.info.get("epsTrailingTwelveMonths")
    pe= (Costo_Accion/eps)

    #P/B 
    pb=Accion.info["priceToBook"]

    #Dividend Yield => DPA/Costo Accion
    dpa=Accion.info["dividendRate"]
    dividend_yield=(dpa/Costo_Accion)*100 #porcentaje

    #Margen de beneficio neto
    ganancia_neta= Accion.financials.loc["Net Income"].iloc[0]
    margen_beneficio=(ganancia_neta/ingresos)*100
    
    return [nombre_empresa,sector,Costo_Accion,porcentaje,descripcion,res_2,ingresos,pe,pb,dividend_yield,margen_beneficio,grafico_ingresos_anuales]

Nombre_Accion="AAPL"
datos=calculo_ratios_metricas(Nombre_Accion)



