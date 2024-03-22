import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class graficos:

    def grafico_expectativa_vida(dataframes, paises):
        plt.figure(figsize=(10, 6))
        for i, df in enumerate(dataframes):
            plt.plot(df['Año'], df['Expectativa de vida'], marker='o', linestyle='-', label=paises[i])
        plt.title('Expectativa de Vida (2000-2019)')
        plt.xlabel('Año')
        plt.ylabel('Expectativa de Vida')
        plt.legend()
        plt.grid(True)
        plt.show()

    def diagrama_dispersion(dataframes, paises, variables):
        plt.figure(figsize=(15, 10))
        for var in variables:
            for i, df in enumerate(dataframes):
                plt.scatter(df['Expectativa de vida'], df[var], label=f"{paises[i]} - {var}")
        plt.title('Diagrama de Dispersión entre Expectativa de Vida y Otras Variables')
        plt.xlabel('Expectativa de Vida')
        plt.legend()
        plt.grid(True)
        plt.show()

    def mapa_calor_correlacion(dataframes, paises):
        for i, df in enumerate(dataframes):
            correlation_matrix = df.corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title(f'Mapa de Calor de Correlación - {paises[i]}')
            plt.show()

    def grafico_tendencia_variables(dataframes, paises, variables):
        plt.figure(figsize=(12, 8))
        for i, df in enumerate(dataframes):
            for var in variables:
                plt.plot(df['Año'], df[var], marker='o', linestyle='-', label=f"{paises[i]} - {var}")
        plt.title('Tendencia de Variables a lo largo del Tiempo')
        plt.xlabel('Año')
        plt.ylabel('Valor de Variables')
        plt.legend()
        plt.grid(True)
        plt.show()

# # Leer los archivos CSV para cada país y almacenarlos en una lista de DataFrames
# data_Peru = pd.read_csv("Data_Perú.csv", sep=';')
# data_RD = pd.read_csv("Data_RD.csv", sep=';')

# # Convertir las columnas de objeto a numéricas
# data_Peru = data_Peru.apply(pd.to_numeric, errors='ignore')
# data_RD = data_RD.apply(pd.to_numeric, errors='ignore')

# # Definir una lista de DataFrames y una lista de nombres de países
# dataframes = [data_Peru, data_RD]
# paises = ['Perú', 'Rep. Dom.']

# # Llamar a las funciones pasando la lista de DataFrames y la lista de nombres de países como argumentos
# grafico_expectativa_vida(dataframes, paises)
# variables = ['Acceso a Atencion medica (%)', 'Calidad del agua (%)', 'Nutricion (Indice de desnutricion)',
#              'Educacion (Tasa de alfabetizacion)', 'Politicas de salud publica (Indice)']
# diagrama_dispersion(dataframes, paises, variables)
# mapa_calor_correlacion(dataframes, paises)
# grafico_tendencia_variables(dataframes, paises, variables)
