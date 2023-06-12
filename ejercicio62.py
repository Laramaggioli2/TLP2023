lista = []
while True:
    numero = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
    if numero == 0:
        break
    lista.append(numero)
print("Tamaño de la lista:", len(lista))
