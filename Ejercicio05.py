import sys
def obtener_n_valido():
    while True:
        try:
            entrada = input("Introduce un número entero N (mayor o igual a 3): ")
            n = int(entrada)
            if n >= 3:
                return n
            else:
                print(f"Error: El número debe ser mayor o igual a 3. Introduciste {n}.")
        except ValueError:
            print(f"Error: Entrada inválida. '{entrada}' no es un número entero válido.")
        except EOFError:
            print("\nEntrada interrumpida. Saliendo del programa.")
            sys.exit(1)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            sys.exit(1)

def generar_matriz_espiral(n):
    matriz = [[0] * n for _ in range(n)]
    fila_inicio, fila_fin = 0, n - 1
    col_inicio, col_fin = 0, n - 1
    contador = 1
    
    while fila_inicio <= fila_fin and col_inicio <= col_fin:
        
        # 1. De Izquierda a Derecha (Fila Superior)
        for j in range(col_inicio, col_fin + 1):
            matriz[fila_inicio][j] = contador
            contador += 1
            fila_inicio += 1
        if fila_inicio > fila_fin:
            break
        # 2. De Arriba a Abajo (Columna Derecha)
        for i in range(fila_inicio, fila_fin + 1):
            matriz[i][col_fin] = contador
            contador += 1
            col_fin -= 1
        if col_inicio > col_fin:
            break
        # 3. De Derecha a Izquierda (Fila Inferior)
        for j in range(col_fin, col_inicio - 1, -1):
            matriz[fila_fin][j] = contador
            contador += 1
            fila_fin -= 1
        if fila_inicio > fila_fin:
            break
        # 4. De Abajo a Arriba (Columna Izquierda)
        for i in range(fila_fin, fila_inicio - 1, -1):
            matriz[i][col_inicio] = contador
            contador += 1
            col_inicio += 1
    return matriz

def imprimir_matriz(matriz):
    if not matriz:
        print("La matriz está vacía.")
        return
    n = len(matriz)
    max_valor = n * n
    ancho = len(str(max_valor))
    print("\nMatriz Espiral:")
    for fila in matriz:
        linea = " ".join(f"{num:>{ancho}}" for num in fila)
        print(linea)

def main():
    print("=== Generador de Matriz Espiral ===")
    n = obtener_n_valido()
    print(f"\nGenerando una matriz de {n} x {n}...")
    matriz_espiral = generar_matriz_espiral(n)
    imprimir_matriz(matriz_espiral)

if __name__ == "__main__":
    main()