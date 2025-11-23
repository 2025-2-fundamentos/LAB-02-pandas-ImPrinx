"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """

    # Se define la ruta del archivo.
    ruta_archivo = 'files/input/tbl2.tsv'
    
    # Se lee el archivo tsv en un DataFrame.
    df = pd.read_csv(ruta_archivo, sep='\t')
    
    # Se crea una columna temporal uniendo 'c5a' y 'c5b' con ':'.
    # Es necesario convertir 'c5b' a string para poder unir.
    df['c5_completa'] = df['c5a'] + ':' + df['c5b'].astype(str)
    
    # Se agrupa por 'c0'. Para cada grupo, se toman los valores de la
    # columna recién creada, se ordenan y se unen con ','.
    df_agrupado = df.groupby('c0')['c5_completa'].apply(lambda x: ','.join(sorted(x)))
    
    # Se convierte la Serie a DataFrame y se resetea el índice.
    resultado = df_agrupado.reset_index()
    
    # Se renombran las columnas para que coincidan con la salida esperada.
    resultado.columns = ['c0', 'c5']
    
    return resultado

# --- Bloque para ejecución y prueba ---
# Se llama a la función y se imprime el resultado.
# resultado = pregunta_12()
# print(resultado)