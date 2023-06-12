sueldos = []
prom=0
for i in range(5):
    sueldo=float(input("Ingrese el sueldo del operario {}: "))
    sueldos.append(sueldo)
    prom=prom+sueldos[i]
print("Lista de sueldos:", sueldos)
prom=prom/5
print("El promedio de los sueldos es de:",prom)

