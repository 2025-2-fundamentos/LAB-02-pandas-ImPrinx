"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se agrupa el DataFrame por la columna 'c1'.
    # Luego, se selecciona la columna 'c2' y se calcula la suma para cada grupo.
    suma_por_letra = df.groupby('c1')['c2'].sum()
    
    return suma_por_letra

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_07()
# print(resultado)