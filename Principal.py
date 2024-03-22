from OrganizarData import Organiza_And_Limpia_Data as OyLData
from Grafico import graficos
import pandas as pd

dataframes = []

#Esta parte fue cambiendo a medida de las necesidades mientras haciamos la diapositiva.

ObjData = OyLData('Data_RD.csv')
dataframes.append(ObjData.limpiar_organizar_datos())
paises = ['Rep. Dom.']

#ObjGrafico = graficos()
#graficos.analisis_factores_comunes(dataframes, paises)
#graficos.grafico_expectativa_vida(dataframes, paises)

variables = ['Calidad del agua (%)','Politicas de salud publica (Indice)']
#graficos.diagrama_dispersion(dataframes, paises, variables)

graficos.grafico_tendencia_variables(dataframes, paises, variables)
