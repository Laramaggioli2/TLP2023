a=int(input("Ingrese la cantidad de piezas: "))
x=1
y=0
while x<=a:
    b=float(input("Ingrese la longitud de las piezas "))
    if b>=1.20 and b<=1.30:
        print("La pieza es apta")
        y=y+1
    x=x+1
print("La cantidad de piezas aptas son: ",y)
