import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
 
sueldos = []


def asignar_sueldo():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for trabajadores in range(10)]
    print("Sueldos asignados aleatoriamente")

def clasificar_sueldo():
    menor_800k = []
    entre_800k_y_2M = []
    mayor_a_2M = []

    for i in range(len(sueldos)):
        if sueldos[i] < 800000:
            menor_800k.append((trabajadores[i], sueldos[i]))
        elif 800000 <= sueldos[i] <= 2000000:
            entre_800k_y_2M.append((trabajadores[i], sueldos[i]))
        else:
            mayor_a_2M.append((trabajadores[i], sueldos[i]))
        
    total_sueldos = sum(sueldos)

    print("\nSueldos menores a $800.000. TOTAL: ", len(menor_800k))
    for trabajador, sueldo in menor_800k:
        print(f"{trabajador:20} ${sueldo:10}")
    
    print("\nSueldos entre $800.000 y 2.000.000, TOTAL: ", len(entre_800k_y_2M))
    for trabajador, sueldo in entre_800k_y_2M:
        print(f"{trabajador:20} ${sueldo:10}")

    print("\nSueldos superiores a 2.000.000, TOTAL =", len(mayor_a_2M))
    for trabajador, sueldo in mayor_a_2M:
        print(f"{trabajador:20} ${sueldo:10}")
    
    print(f"\nTOTAL SUELDOS = ${total_sueldos}")

def ver_stats():
    if not sueldos:
        print("No hay ningún sueldo asignado.")
        return
    
    sueldo_mas_low = min(sueldos)
    sueldo_mas_high = max(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica = math.prod(sueldos) ** (1 / len(sueldos))

    print("\nEstadisticas de sueldos:")
    print(f"Sueldo más bajo: ${sueldo_mas_low}")
    print(f"Sueldo más alto: ${sueldo_mas_high}")
    print(f"Promedio de sueldos: ${promedio_sueldos: .2f}")
    print(f"Media geométrica: ${media_geometrica: .2f}")

def report_sueldos():
    if not sueldos:
        print("No hay ningún sueldo asignado.")
        return
    
    descuentos_salud = [sueldo * 0.07 for sueldo in sueldos]
    descuentos_afp = [sueldo * 0.12 for sueldo in sueldos]
    sueldos_liquidos = [sueldo - salud - afp for sueldo, salud, afp in zip(sueldos, descuentos_salud, descuentos_afp)]

    with open("reporte_sueldos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo liquido"])
        for i in range(len(trabajadores)):
            writer.writerow([trabajadores[i], sueldos[i], descuentos_salud[i], descuentos_afp[i], sueldos_liquidos[i]])

            print("\nReporte de sueldos:")
            for i in range(len(trabajadores)):
                print(f"{trabajadores[i]:20} Sueldo base: ${sueldos[i]}")
                print(f"Descuento salud: ${descuentos_salud[i]:.2f}")
                print(f"Sueldo liquido: ${sueldos_liquidos[i]:.2f}")
                print()
            print("Reporte exportado a reporte_sueldos.csv")


def main_menu():
    print('''
    
    -------------------------------
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadisticas
    4. Reporte de sueldos
    5. Salir del programa
    -------------------------------
          
          ''')

while True:
    main_menu()
    opcion = input("Seleccione una opción del 1 al 5:")

    if opcion == "1":
        asignar_sueldo()
    elif opcion == "2":
        clasificar_sueldo()
    elif opcion == "3":
        ver_stats()
    elif opcion == "4":
        report_sueldos()
    elif opcion == "5":
        print("Finalizando programa...")
        print("Desarrollado por Cristóbal Zamorano")
        print("RUT: 21.625.936-K")
        break
    else:
        print("Opción no válida, intentelo de nuevo.")
if __name__ == "__main__":
    main_menu()
    