def calcular_salario(salario_base, horas_extras, pago_hora_extra, bono, afp, salud):

    # 1. Cálculo del Salario Bruto (sin descuentos)
    salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono

    # 2. Cálculo de Descuentos
    descuento_afp = salario_base * (afp / 100)
    descuento_salud = salario_base * (salud / 100)
    descuentos_totales = descuento_afp + descuento_salud

    # 3. Cálculo del Salario Neto
    salario_neto = salario_bruto - descuentos_totales

    return salario_bruto, descuentos_totales, salario_neto

salario_base_ejemplo = 1500.00
horas_extras_ejemplo = 10
pago_hora_extra_ejemplo = 15.00
bono_ejemplo = 50.00
afp_porcentaje = 13.0 
salud_porcentaje = 7.0 

bruto, descuentos, neto = calcular_salario(
    salario_base_ejemplo,
    horas_extras_ejemplo,
    pago_hora_extra_ejemplo,
    bono_ejemplo,
    afp_porcentaje,
    salud_porcentaje
)

print("--- Cálculo de Salario ---")
print(f"Salario Base: ${salario_base_ejemplo:,.2f}")
print(f"Pago por Horas Extras: ${(horas_extras_ejemplo * pago_hora_extra_ejemplo):,.2f}")
print(f"Bono Adicional: ${bono_ejemplo:,.2f}")
print("-" * 30)
print(f"Salario Bruto (sin descuentos): ${bruto:,.2f}")
print(f"Descuentos Totales (AFP + Salud): ${descuentos:,.2f}")
print("-" * 30)
print(f"Salario Neto (a recibir): ${neto:,.2f}")