num1=int(input("Ingrese una cantidad de triángulos a registrar: "))
isosceles=0
escaleno=0
equilatero=0
for x in range (num1) :
    lados=int(input("ingrse cantidad de lados del triangulo: "))
    a=int(input("Ingrese lado del triángulo: "))
    b=int(input("Ingrese lado del triángulo: "))
    c=int(input("Ingrese lado del triángulo: "))
    if a == b and b == c:
        print("El triángulo es equilátero")
        equilatero += 1
    else:
        
        if a == b or b == c or a == c:
            print("El triángulo es isósceles")
            isosceles += 1
        else:
            print("El triángulo es escaleno")
            escaleno += 1
print ("La cantidad de triángulos equiláteros que hay son: ",equilatero)
print ("La cantidad de triángulos isósceles que hay son: ",isosceles)
print ("La cantidad de triángulos escalenos que hay son: ",escaleno)
