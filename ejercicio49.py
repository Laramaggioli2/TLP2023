nombre = input("Ingrese un nombre: ")
caracter = nombre[0].lower()
if caracter in ['a', 'e', 'i', 'o', 'u']:
    print("El nombre empieza con una vocal.")
else:
    print("El nombre no empieza con una vocal.")
