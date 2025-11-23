"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl1.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se agrupa por la primera columna ('c0'). Para cada grupo, se toman los
    # valores de 'c4', se ordenan alfabéticamente y se unen con una coma.
    df_agrupado = df.groupby('c0')['c4'].apply(lambda x: ",".join(sorted(x)))
    
    # Se convierte la Serie resultante a un DataFrame y se resetea el índice.
    resultado = df_agrupado.reset_index()
    
    # Se renombran las columnas para que coincidan con la salida esperada.
    resultado.columns = ['c0', 'c4']
    
    return resultado

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_11()
# print(resultado)