import math
def _calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def _calcular_desviacion_estandar(lista, media):
    n = len(lista)
    if n <= 1:
        return 1.0 if n == 1 else 0.0
    sum_sq_diff = sum([(x - media) ** 2 for x in lista])
    return math.sqrt(sum_sq_diff / (n - 1))

def _calcular_norma(lista):
    sum_sq = sum([x ** 2 for x in lista])
    return math.sqrt(sum_sq)

def normalizar(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        raise ValueError(f"Modo de normalización no válido: '{modo}'. Debe ser 'minmax', 'zscore' o 'unit'.")
    nueva_lista = []
    if not lista:
        return []
    if modo == "minmax":
        min_val = min(lista)
        max_val = max(lista)
        rango = max_val - min_val
        
        if rango == 0:
            nueva_lista = [0.0] * len(lista)
        else:
            nueva_lista = [(x - min_val) / rango for x in lista]

    elif modo == "zscore":
        media = _calcular_media(lista)
        desv_est = _calcular_desviacion_estandar(lista, media)
        
        if desv_est == 0:
            nueva_lista = [0.0] * len(lista)
        else:
            nueva_lista = [(x - media) / desv_est for x in lista]

    elif modo == "unit": 
        norma = _calcular_norma(lista)
        
        if norma == 0:
            nueva_lista = [0.0] * len(lista)
        else:
            nueva_lista = [x / norma for x in lista]
            
    return nueva_lista

print("## Versión 1: Python Puro ##")
valores = [10, 20, 30]
salida_minmax = normalizar(valores, "minmax")
print(f"Minmax: {salida_minmax}") 
salida_zscore = normalizar(valores, "zscore")
print(f"Zscore: {salida_zscore}") 
salida_unit = normalizar(valores, "unit")
print(f"Unit: {salida_unit}") 
print(f"Original: {valores}")
valores_cero_div = [5, 5, 5]
print(f"Prueba Div/0 (Minmax): {normalizar(valores_cero_div, 'minmax')}")
print(f"Prueba Div/0 (Zscore): {normalizar(valores_cero_div, 'zscore')}")
print(f"Prueba Div/0 (Unit): {normalizar([0, 0, 0], 'unit')}")