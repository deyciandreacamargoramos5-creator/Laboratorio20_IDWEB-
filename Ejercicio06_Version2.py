import numpy as np
def normalizar_numpy(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        raise ValueError(f"Modo de normalización no válido: '{modo}'. Debe ser 'minmax', 'zscore' o 'unit'.")
    arr = np.array(lista, dtype=float)
    if arr.size == 0:
        return []

    if modo == "minmax":
        min_val = arr.min()
        max_val = arr.max()
        rango = max_val - min_val
    
        if rango == 0:
            arr_normalizado = np.zeros_like(arr)
        else:
            arr_normalizado = (arr - min_val) / rango
    elif modo == "zscore":
        media = arr.mean()
        desv_est = arr.std(ddof=0)
        if desv_est == 0:
            arr_normalizado = np.zeros_like(arr)
        else:
            arr_normalizado = (arr - media) / desv_est

    elif modo == "unit": 
        norma = np.linalg.norm(arr)
        
        if norma == 0:
            arr_normalizado = np.zeros_like(arr)
        else:
            arr_normalizado = arr / norma
            
    return arr_normalizado.tolist()

print("## Versión 2: Con NumPy ##")
valores = [10, 20, 30]
salida_minmax_np = normalizar_numpy(valores, "minmax")
print(f"Minmax: {salida_minmax_np}") 
salida_zscore_np = normalizar_numpy(valores, "zscore")
print(f"Zscore: {salida_zscore_np}") 
salida_unit_np = normalizar_numpy(valores, "unit")
print(f"Unit: {salida_unit_np}") 
print(f"Original: {valores}")
valores_cero_div = [5, 5, 5]
print(f"Prueba Div/0 (Minmax): {normalizar_numpy(valores_cero_div, 'minmax')}")
print(f"Prueba Div/0 (Zscore): {normalizar_numpy(valores_cero_div, 'zscore')}")
print(f"Prueba Div/0 (Unit): {normalizar_numpy([0, 0, 0], 'unit')}")