mañana = []
tarde = []

print("Ingreso de sueldos de empleados - Turno mañana")
for i in range(4):
    sueldo = float(input("Ingrese el sueldo del empleado {}: "))
    mañana.append(sueldo)

print("\nIngreso de sueldos de empleados - Turno tarde")
for i in range(4):
    sueldo = float(input("Ingrese el sueldo del empleado {}: "))
    tarde.append(sueldo)

print("\nLista de sueldos - Turno mañana:")
for sueldo in mañana:
    print(sueldo)

print("\nLista de sueldos - Turno tarde:")
for sueldo in tarde:
    print(sueldo)
