def calculadora_impuestos_progresivos():
   
    tramos = [
        (20000, 0.00),   
        (50000, 0.10),   
        (100000, 0.20),  
        (float('inf'), 0.30) 
    ]

    while True:
        try:
            ingreso_mensual = float(input("Ingrese el ingreso mensual: $"))
            if ingreso_mensual >= 0:
                break
            else:
                print("El ingreso debe ser un valor positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    ingreso_anual = ingreso_mensual * 14
    
    ingreso_restante = ingreso_anual
    total_impuestos = 0
    limite_inferior = 0

    print("\n--- Resultados del Cálculo de Impuestos ---")
    print(f"Ingreso Mensual Ingresado: ${ingreso_mensual:,.2f}")
    print(f"Ingreso Anual Gravable (14 sueldos): ${ingreso_anual:,.2f}\n")

    for limite_superior, tasa in tramos:
        
        if ingreso_restante > 0:
            
            monto_del_tramo = limite_superior - limite_inferior
            
            base_gravable = min(ingreso_restante, monto_del_tramo)
            
            impuesto_tramo = base_gravable * tasa
            total_impuestos += impuesto_tramo

            print(f"Impuesto por Tramo [{limite_inferior:,.0f} – {limite_superior:,.0f}]:")
            print(f"   Base Gravable: ${base_gravable:,.2f}")
            print(f"   Tasa Aplicada: {tasa * 100:.0f}%")
            print(f"   Impuesto Calculado: ${impuesto_tramo:,.2f}")

            ingreso_restante -= base_gravable
            limite_inferior = limite_superior
        
        if ingreso_restante <= 0:
            break

    print("\n" + "=" * 40)
    print(f"Total de Impuestos Anuales: ${total_impuestos:,.2f}")
    
    if ingreso_anual > 0:
        tasa_efectiva = (total_impuestos / ingreso_anual) * 100
        print(f"Tasa Efectiva Real (Impuesto/Ingreso): {tasa_efectiva:.2f}%")
    else:
        print("Tasa Efectiva Real: 0.00%")
    print("=" * 40)
calculadora_impuestos_progresivos()