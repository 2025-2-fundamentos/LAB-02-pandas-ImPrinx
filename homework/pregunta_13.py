"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    # Se definen las rutas de los archivos.
    ruta_tbl0 = 'files/input/tbl0.tsv'
    ruta_tbl2 = 'files/input/tbl2.tsv'
    
    # Se leen ambos archivos en DataFrames de pandas.
    df0 = pd.read_csv(ruta_tbl0, sep='\t')
    df2 = pd.read_csv(ruta_tbl2, sep='\t')
    
    # Se unen (merge) los dos DataFrames usando 'c0' como la clave común.
    # Esto crea una tabla combinada donde las filas con el mismo 'c0' se alinean.
    df_merged = pd.merge(df0, df2, on='c0')
    
    # Sobre la tabla combinada, se agrupa por la columna 'c1' (de tbl0)
    # y se calcula la suma de la columna 'c5b' (de tbl2) para cada grupo.
    resultado = df_merged.groupby('c1')['c5b'].sum()
    
    return resultado

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_13()
# print(resultado)