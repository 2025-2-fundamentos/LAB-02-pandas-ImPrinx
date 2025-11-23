"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    # Se define la ruta del archivo.
    # Nota: El enunciado menciona tbl1.csv, pero el archivo cargado es tbl1.tsv.
    ruta_archivo = 'files/input/tbl1.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se convierte la columna 'c4' a mayúsculas, se obtienen los valores únicos
    # y se convierte el resultado a una lista ordenada.
    lista_ordenada = sorted(df['c4'].str.upper().unique())
    
    return lista_ordenada

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_06()
# print(resultado)