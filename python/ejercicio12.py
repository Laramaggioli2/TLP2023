sueldo= int(input("Ingrese el sueldo del empleado: "))
antiguedad= int(input("Ingrese la antiguedad del empleado: "))
if sueldo<500 and antiguedad>=10:
    total=sueldo+((sueldo*20)/100)
    print("Se le agregará un 20% a su sueldo: ",total)
if sueldo<500 and antiguedad<10:
    total=sueldo+((sueldo*5)/100)
    print("Se le agregará un 5% a su sueldo: ",total)
if sueldo>=500:
    print("Su sueldo no será modificado: ",sueldo)
