"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv con pandas. El separador es un tabulador ('\t').
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se retorna la cantidad de filas del DataFrame.
    # len(df) o df.shape[0] son dos formas de obtenerlo.
    cantidad_filas = len(df)
    
    return cantidad_filas

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_01()
# print(f"La cantidad de filas en tbl0.tsv es: {resultado}")