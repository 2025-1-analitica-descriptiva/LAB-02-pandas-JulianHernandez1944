"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    import pandas as pd
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep='\t')
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep='\t')
    # Agrupar tbl2 por c0 y c1, y sumar c5b
    result = tbl2.groupby('c0')['c5b'].sum().reset_index()
    # Unir tbl0 y el resultado por c0
    result = pd.merge(tbl0[['c0', 'c1']], result, on='c0')
    # Agrupar por c1 y sumar c5b
    result = result.groupby('c1')['c5b'].sum()
    return result
if __name__ == '__main__':
    print(pregunta_13())
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
