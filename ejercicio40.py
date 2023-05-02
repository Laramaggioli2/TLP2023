a=10
negativo=0
positivo=0
multiplo=0
par=0
suma=0
for x in range (a) :
    num=int(input("Ingrse un valor: "))
    if num<0:
        negativo+= 1
    else:
        positivo+= 1

    if num%15==0:
        multiplo+= 1

    if num%2==0:
        par+= 1
        suma= suma+num
print ("La cantidad de números positivos son : ",positivo)
print ("La cantidad de números negativos son : ",negativo)
print ("La cantidad de números múltiplos de 15 son : ",multiplo)
print ("La acumulación de los números pares es : ",suma)

    

