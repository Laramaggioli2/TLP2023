num1=int(input("Ingrese una cantidad de números a ingresar:"))
contador=0
for x in range (num1):
    a=int(input("Ingrese los números: "))
    if a>=1000:
       contador=contador+1
print ("La cantidad de números mayores o iguales a 1000 son: ",contador)
