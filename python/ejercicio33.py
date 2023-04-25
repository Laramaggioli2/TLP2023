contador=0
contador1=0
for x in range (10):
    a=int(input("Ingrese 10 números: "))
    if a%5==0:
       contador=contador+1
    if a%3==0:
        contador1=contador1+1
print ("Los valores ingresados son múltiplos de 5 son: ",contador)
print ("Los valores ingresados no son múltiplos de 3 son: ",contador1)
