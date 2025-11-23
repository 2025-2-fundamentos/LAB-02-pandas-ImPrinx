"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv con pandas.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se retorna la cantidad de columnas del DataFrame.
    # df.shape retorna una tupla (filas, columnas). Accedemos al segundo elemento.
    cantidad_columnas = df.shape[1]
    
    return cantidad_columnas

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_02()
# print(f"La cantidad de columnas en tbl0.tsv es: {resultado}")