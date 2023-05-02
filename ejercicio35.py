num1=int(input("Ingrese una cantidad de pares a registrar: "))
contador=0
superficie=0
for contador in range (num1):
    base=int(input("Ingrese la base del triángulo: "))
    altura=int(input("Ingrese la altura del triángulo: "))
    superficie= (base*altura)/2
    print("La base del triángulo es ",base,", la altura es ",altura,", y la superficie es ",superficie)
    if superficie>12:
        contador=contador+1
        print("La cantidad de triángulos con superficie mayor a 12 son: ")
        
    
 
    
    
