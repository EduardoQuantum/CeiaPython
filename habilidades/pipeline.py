# habilidades/pipeline.py
# Habilidad: herramientas para el pipeline de datos
# (Es la misma logica de las funciones include() y log() de la Clase 05,
# agrupadas en una clase llamada PipelineTools.)
#
# En el fondo, PipelineTools es una clase con dos metodos: include() y log().
# La llamamos "habilidad" porque resuelve una tarea concreta del pipeline
# y se puede importar en cualquier proyecto.

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
        # no con las de este archivo. Asi, base_trabajo, pd, np, etc. estan
        # disponibles exactamente como en la Clase 05.
        with open(archivo, "r") as f:
            codigo = f.read()
        exec(codigo, self.namespace)

    def log(self, archivo, contenido):
        # Guarda contenido en un archivo de texto.
        with open(archivo, "w") as f:
            f.write(contenido)
