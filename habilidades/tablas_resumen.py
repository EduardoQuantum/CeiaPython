# habilidades/tablas_resumen.py
# Habilidad: tablas resumen con estadisticas descriptivas
#
# Ofrece dos metodos rapidos para explorar una base de datos:
# resumen_numericas() para columnas numericas
# resumen_categoricas() para columnas de texto

import pandas as pd
import numpy as np

class tablas_resumen:

    def __init__(self, base):
        # Guardamos la base de trabajo
        self.base = base.copy()

    def resumen_numericas(self):
        # Devuelve un cuadro con media, desvio, minimo, maximo y cuartiles
        # de todas las columnas numericas de la base
        numericas = self.base.describe().round(2)
        return numericas

    def resumen_categoricas(self):
        # Devuelve la frecuencia de cada valor para cada columna de texto
        categoricas = self.base.select_dtypes(include=['object', 'category'])
        resumen = {}
        for col in categoricas.columns:
            resumen[col] = categoricas[col].value_counts()
        return resumen
