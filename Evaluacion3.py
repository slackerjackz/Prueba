import csv
import os

CargosValidos = ["Mesero","Cocinero","Cajero"]
FileTrabajadores = "trabajadores.csv"

trabajadores = []

def loadWorkersFromFile():
    global trabajadores
    if os.path.exists(FileTrabajadores):
        with open(FileTrabajadores, mode='r', newline='',encoding='utf-8') as file:
         reader = csv.reader(file)
         trabajadores = list(reader)
def saveWorkersOnFile():
   with open(FileTrabajadores, mode='w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerows(trabajadores)
def calculoDescuentosyLiquid(sueldo_bruto):
   descuento_salud = 0.07 * sueldo_bruto
   descuento_afp = 0.10 * sueldo_bruto
   sueldo_liquido = sueldo_bruto - descuento_salud - descuento_afp
   return descuento_salud, descuento_afp, sueldo_liquido

def registroWorkers():
   nombre = input("ingrese el nombre del trabajador: ")
   apellido = input("Ingrese el apellido del trabajador: ")
   cargo = input("Ingrese el cargo del trabajador (Mesero, Cocinero o Cajero): ").lower()
   while cargo not in CargosValidos:
      print("Cargo ingresado no válido. Los cargos validos son: Mesero, Cocinero, Cajero")
      cargo = input("Ingrese el cargo del trabajador nuevamente: ").lower()
      sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))

      descuento_salud, descuento_afp, sueldo_liquido = calculoDescuentosyLiquid(sueldo_bruto)

      trabajadores.append([nombre, apellido, cargo, sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido])

      saveWorkersOnFile()

      print("Trabajador registrado correctamente")

def listarWorkers():
   if not trabajadores:
      print("No hay empleados registrados")
   else:
      for trabajador in trabajadores:
         nombre, apellido, cargo, sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido = trabajador
         print(f"Nombre: {nombre} {apellido}, Cargo: {cargo}, Sueldo Bruto: {sueldo_bruto}")
         print(f"Descuento Salud: {descuento_salud}, Descuento de AFP: {descuento_afp}")
         print(f"Sueldo Liquido: {sueldo_liquido}")


def impresionPlanilla():
   cargo_seleccionado = input("Ingrese el cargo para la impresión de la planilla (Mesero, Cocinero o Cajero): ").lower()
   while cargo_seleccionado not in CargosValidos:
      print("Cargo ingresado no válido, Los cargos válidos son: Mesero, Cocinero, Cajero")
      cargo_seleccionado = input("Ingrese el cargo nuevamente:").lower()

      trabajadores_cargo = [trabajador for trabajador in trabajadores
                            if trabajador [2] == cargo_seleccionado]
      if not trabajadores_cargo:
       print(f"No hay trabajadores registrados como {cargo_seleccionado}")
   else:
      for trabajador in trabajadores_cargo:
         nombre, apellido, cargo, sueldo_bruto, descuento_salud, descuento_afp, sueldo_liquido = trabajador
         print(f"Nombre: {nombre} {apellido}, Sueldo Bruto: {sueldo_bruto}")
         print(f"Descuento Salud: {descuento_salud}")
         print(f"Descuento AFP: {descuento_afp}")
         print(f"Sueldo Liquido: {sueldo_liquido}")


def menu_main():
   print("Bienvenido a la aplicación de Registro")
   while True:
      print("---Opciones---")
      print("1. Registrar Trabajador")
      print("2. Enlistar todos los trabajadores")
      print("3. Imprimir planilla por Cargo")
      print("4. Salir")

      opcion = input("Seleccione una de las opciones (1-4): ")
      if opcion == "1":
         registroWorkers()
         continue
      elif opcion == "2":
         listarWorkers()
         continue
      elif opcion == "3":
         impresionPlanilla()
         continue
      elif opcion == "4":
         print("Tenga un buen día")
         break
      else:
         print("Opción no válida, ingrese un numero del 1 al 4")

loadWorkersFromFile()

menu_main()