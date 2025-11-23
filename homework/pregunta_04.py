"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se agrupa el DataFrame por la columna 'c1'.
    # Luego, se selecciona la columna 'c2' y se calcula el promedio para cada grupo.
    promedio_por_letra = df.groupby('c1')['c2'].mean()
    
    return promedio_por_letra

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_04()
# print(resultado)