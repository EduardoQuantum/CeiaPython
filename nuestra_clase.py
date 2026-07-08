# nuestra_clase.py
# Clases auxiliares para el pipeline:
#   - PipelineTools: incluye include() y log() de la Clase 05
#   - formatos_copados: encapsula la pivot_table de la Clase 04
# Se importan con: from nuestra_clase import PipelineTools, formatos_copados

import pandas as pd
import numpy as np

class PipelineTools:

    def __init__(self, base, namespace):
        # Guardamos la base como atributo del objeto
        self.base = base.copy()
        # Guardamos las globals del script que llama.
        # Asi, include() ve las mismas variables que ve el script principal
        # (base_trabajo, pd, np, etc.), igual que en la Clase 05.
        self.namespace = namespace

    def include(self, archivo):
        # Inyecta codigo desde un archivo externo.
        # El codigo inyectado se ejecuta con las globals del script que llamo,
        # no con las de nuestra_clase.py. Asi, base_trabajo, pd, np, etc. estan
        # disponibles exactamente como en la Clase 05.
        with open(archivo, "r") as f:
            codigo = f.read()
        exec(codigo, self.namespace)

    def log(self, archivo, contenido):
        # Guarda contenido en un archivo de texto.
        with open(archivo, "w") as f:
            f.write(contenido)


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
