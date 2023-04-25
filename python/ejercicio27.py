a=int(input("Ingrese una cantidad de números enteros: "))
x=1
y=0
while x<=a:
    b=float(input("Ingrese los números enteros: "))
    if b%2==0:
        print("El número es par: ",b)
        y=y+1
    else:
        print("El número es impar: ",b)
    x=x+1
