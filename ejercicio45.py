num1=int(input("Ingrese un valor: "))
a=input("¿Desea Ingresar otro valor? (si/no) ")
b= "si"
c="no"
suma=0
if a==b:
    num2=int(input("Ingrese otro valor: "))
    suma=num1+num2
    print("La suma de los valores es: ",suma)
else:
    if a==c:
        print("Operación finalizada.")
        
