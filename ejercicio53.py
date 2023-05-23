vocal='a', 'e', 'i', 'o', 'u'
contador=0
oracion=input("Ingrese una oración: ")
for letra in oracion:
        if letra in vocal:
            contador += 1
cadena1=oracion.upper();
print(cadena1)
print("Cantidad de vocales:", contador)
