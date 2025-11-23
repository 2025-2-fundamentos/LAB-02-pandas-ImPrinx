"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se selecciona la columna 'c1' y se cuenta la frecuencia de cada valor.
    conteo = df['c1'].value_counts()
    
    # Se ordena el resultado por el índice (las letras) alfabéticamente.
    resultado_ordenado = conteo.sort_index()
    
    return resultado_ordenado

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_03()
# print(resultado)