# habilidades/formatos.py
# Habilidad: herramientas para generar tablas y reportes
# (Es la pivot_table de la Clase 04, encapsulada en una clase
# llamada formatos_copados.)
#
# En el fondo, formatos_copados es una clase con un metodo: reporte_tabla().
# La llamamos "habilidad" porque resuelve la tarea de generar tablas cruzadas
# y se puede importar en cualquier proyecto.

import pandas as pd
import numpy as np

class formatos_copados:

    def __init__(self, base):
        # Guardamos la base de trabajo
        self.base = base.copy()

    def reporte_tabla(self, fila, columna, valor, estadistico='mean'):
        # Encapsula la pivot_table de la Clase 04.
        # Recibe los parametros editables (fila, columna, valor, estadistico)
        # y devuelve la tabla cruzada formateada.
        df_resumen = self.base.pivot_table(
            index=fila,
            columns=columna,
            values=valor,
            aggfunc=estadistico
        )
        # Redondeo a 2 decimales para que la salida sea legible
        df_resumen = df_resumen.round(2)
        return df_resumen
