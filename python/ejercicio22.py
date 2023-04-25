x=1
y=0
while x<=10:
    b=float(input("Ingrese las 10 notas "))
    if b>=7:
        print("La nota, ",b," es mayor a 7")
        y=y+1
    else:
        print("La nota, ",b," es menor a 7")
    x=x+1
