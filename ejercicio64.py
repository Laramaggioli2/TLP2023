def obtener_promedio(alturas):
    return sum(alturas) / len(alturas)

def contar_personas_altas_bajas(alturas, promedio):
    altas = 0
    bajas = 0
    for altura in alturas:
        if altura > promedio:
            altas += 1
        elif altura < promedio:
            bajas += 1
    return altas, bajas

alturas = []
for i in range(5):
    altura = float(input("Ingrese la altura de la persona {}: ".format(i+1)))
    alturas.append(altura)

promedio = obtener_promedio(alturas)
print("El promedio de las alturas es: {:.2f}".format(promedio))

altas, bajas = contar_personas_altas_bajas(alturas, promedio)
print("Personas más altas que el promedio: {}".format(altas))
print("Personas más bajas que el promedio: {}".format(bajas))
