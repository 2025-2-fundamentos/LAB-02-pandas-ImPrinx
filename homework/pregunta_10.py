"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl0.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se agrupa por 'c1'. Para cada grupo en 'c2':
    # 1. Se ordenan los números.
    # 2. Se convierten a string.
    # 3. Se unen con ':'.
    # El resultado es una Serie de pandas.
    df_agrupado = df.groupby('c1')['c2'].apply(lambda x: ":".join(map(str, sorted(x))))

    # Para que el resultado sea un DataFrame como en la Rta/ (aunque la Rta/
    # es técnicamente una Serie), lo convertimos a DataFrame.
    resultado = df_agrupado.to_frame()

    return resultado

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_10()
# print(resultado)