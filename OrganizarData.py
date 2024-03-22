import pandas as pd

class Organiza_And_Limpia_Data:

    def __init__(self, filename):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            # Le ponemos nombres a las columnas
            self.column_names = ['Año', 'Expectativa de vida', 'Acceso a Atencion medica (%)', 'Calidad del agua (%)',
                                 'Nutricion (Indice de desnutricion)', 'Educacion (Tasa de alfabetizacion)',
                                 'Politicas de salud publica (Indice)', 'Indice de desarrollo Humano (IDG)']

            # Esto es para leer los datos
            self.data = pd.read_csv(filename, sep=';', names=self.column_names)

    def limpiar_organizar_datos(self):
        # Para eliminar los valores null
        self.data.dropna(inplace=True)

        # Sin esto me daba error, decia que no se podian manipular datos que no sean numericos, xd
        self.data = self.data.apply(pd.to_numeric, errors='ignore')

        # Resetear el índice para eliminar el número al inicio
        self.data.reset_index(drop=True, inplace=True)

        # Devolver los datos limpios
        return self.data
