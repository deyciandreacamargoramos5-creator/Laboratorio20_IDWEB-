import sys

registro_estudiantes = []

def agregar_estudiante():
    print("\n--- Agregar Estudiante ---")
    
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero para la edad.")

    while True:
        try:
            promedio = float(input("Ingrese el promedio del estudiante: "))
            if promedio >= 0:
                break
            else:
                print("El promedio no puede ser negativo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número para el promedio.")

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    
    registro_estudiantes.append(estudiante)
    print(f"\nEstudiante '{nombre}' agregado exitosamente.")

def mostrar_estudiantes():
    print("\n--- Lista de Estudiantes ---")
    if not registro_estudiantes:
        print("El registro está vacío. No hay estudiantes para mostrar.")
        return

    print(f"{'No.':<4}{'Nombre':<20}{'Edad':<8}{'Promedio':<10}")
    print("-" * 42)
    for i, estudiante in enumerate(registro_estudiantes):
        print(
            f"{i+1:<4}"
            f"{estudiante['nombre']:<20}"
            f"{estudiante['edad']:<8}"
            f"{estudiante['promedio']:<10.2f}"
        )

def mostrar_mejor_promedio():
    print("\n--- Estudiante con Mejor Promedio ---")
    if not registro_estudiantes:
        print("El registro está vacío.")
        return

    mejor_estudiante = max(registro_estudiantes, key=lambda x: x['promedio'])
    
    print(f"Estudiante con el promedio más alto:")
    print(f"  Nombre: {mejor_estudiante['nombre']}")
    print(f"  Edad: {mejor_estudiante['edad']} años")
    print(f"  Promedio: {mejor_estudiante['promedio']:.2f}")

def buscar_por_nombre():
    print("\n--- Buscar Estudiante por Nombre ---")
    if not registro_estudiantes:
        print("El registro está vacío.")
        return
        
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    
    resultados = [
        est for est in registro_estudiantes 
        if termino in est['nombre'].lower()
    ]

    if not resultados:
        print(f"No se encontraron estudiantes con el término '{termino}'.")
        return

    print(f"\nResultados de la búsqueda para '{termino}':")
    print(f"{'Nombre':<20}{'Edad':<8}{'Promedio':<10}")
    print("-" * 38)
    for est in resultados:
        print(
            f"{est['nombre']:<20}"
            f"{est['edad']:<8}"
            f"{est['promedio']:<10.2f}"
        )

def eliminar_por_nombre():
    print("\n--- Eliminar Estudiante por Nombre ---")
    if not registro_estudiantes:
        print("El registro está vacío.")
        return

    nombre_eliminar = input("Ingrese el nombre EXACTO del estudiante a eliminar: ").strip()
    
    indice_a_eliminar = -1
    for i, est in enumerate(registro_estudiantes):
        if est['nombre'] == nombre_eliminar:
            indice_a_eliminar = i
            break
            
    if indice_a_eliminar != -1:
        estudiante_eliminado = registro_estudiantes.pop(indice_a_eliminar)
        print(f"\nEstudiante '{estudiante_eliminado['nombre']}' eliminado correctamente.")
    else:
        print(f"Estudiante con nombre '{nombre_eliminar}' no encontrado en el registro.")

def mostrar_menu():
    print("\n===============================")
    print("REGISTRO DE ESTUDIANTES")
    print("===============================")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Mostrar estudiante con mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")
    print("-------------------------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            mostrar_mejor_promedio()
        elif opcion == '4':
            buscar_por_nombre()
        elif opcion == '5':
            eliminar_por_nombre()
        elif opcion == '6':
            print("\n¡Gracias por usar el Registro de Estudiantes! Saliendo del programa.")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 6.")

if __name__ == "__main__":
    main()