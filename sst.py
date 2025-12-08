import yfinance as yf
import pandas as pd

# input("Ingrese el nombre de la accion: ")

Nombre_Accion="AAPL"
Accion = yf.Ticker(Nombre_Accion)
Accion_dividendo=Accion.dividends

Costo_Accion= Accion.info["regularMarketPrice"]
print("Costo de accion")
print(F"${Costo_Accion} ")

#calculo del P/E

eps= Accion.info.get("epsTrailingTwelveMonths")

Pe=(Costo_Accion/eps)
print(f"El P/E es {Pe :2f}")

#Calculo de P/B
PB= Accion.info["priceToBook"]

# print(msft.financials)
# print(msft.balancesheet)

#Calculo del dividendo yield
DPA=Accion.info[]
Dividend_yield=(DPA/Costo_Accion)

print("historial de Dividendos")
print(Accion_dividendo)

