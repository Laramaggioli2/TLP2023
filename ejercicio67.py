lista=[]
for x in range(5):
    valor = int(input("Ingrese un entero: "))
    lista.append(valor)
mayor=lista[0]
posicion = 0
for x in range(1,len(lista)):
    if lista[x] <mayor:
        mayor = lista[x]
        posicion = x

print("El menor valor es:")
print(mayor)
print("Se encuentra en la posición:")
print(posicion)

