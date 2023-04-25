num1=int(input("Ingrese un valor: "))
num2=int(input("Ingrese otro valor: "))
num3=int(input("Ingrese otro valor: "))
if num1>num2 and num1>num3:
    print("El primer valor es el mayor",num1)
else:
    if num1<num2 and num1<num3:
        print("El primer valor es el menor",num1)
if num2>num1 and num2>num3:
        print("El segundo valor es el mayor",num2)
else:
    if num2<num1 and num2<num3:
        print("El segundo valor es el menor",num2)
if num3>num1 and num3>num2:
    print("El tercer valor es el mayor",num3)
else:
    if num3<num1 and num3<num2:
        print("El tercer valor es el menor",num3)

