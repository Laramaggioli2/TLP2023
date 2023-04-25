a=int(input("Ingrese la cantidad de empleados: "))
x=1
y=0
while x<=a:
    b=float(input("Ingrese el sueldo de sus empleados: "))
    if b>=100 and b<=300:
        print("El sueldo del empleado es menor o igual a $300: ",b)
        y=y+1
    else:
        if b>=100 and b<=500:
            print("El sueldo del empleado es mayor a $300: ",b)
    x=x+1

