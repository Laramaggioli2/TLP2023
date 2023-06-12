lista = [ "sofia", "lara", "juliana", "delfina", "sol"]
contador = 0
for nombre in lista:
    if len(nombre) > 5:
        contador += 1
print("Cantidad de nombres con más de 5 caracteres:", contador)
