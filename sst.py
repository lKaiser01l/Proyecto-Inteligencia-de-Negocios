import yfinance as yf
import pandas as pd
import tkinter


Nombre_Accion=input("Ingrese el nombre de la accion: ")
Accion = yf.Ticker(Nombre_Accion)
Accion_dividendo=Accion.dividends

#calculo del P/E

eps= Nombre_Accion.info.get("epsTrailingTwelveMonths")


# print(msft.financials)
# print(msft.balancesheet)
print("Costo de accion")
print(F"${Accion.info["regularMarketPrice"]} ")

print("historial de Dividendos")
print(Accion_dividendo)

print(Accion.info)