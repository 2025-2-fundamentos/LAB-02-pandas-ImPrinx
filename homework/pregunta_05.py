"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se agrupa el DataFrame por la columna 'c1'.
    # Luego, se selecciona la columna 'c2' y se calcula el valor máximo para cada grupo.
    maximo_por_letra = df.groupby('c1')['c2'].max()
    
    return maximo_por_letra

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_05()
# print(resultado)