alumnos=[]
notas=[]
for x in range(5):
    nom=input("Ingrese el nombre del alumno: ")
    alumnos.append(nom)
    no=int(input("Ingrese la nota de dicho alumno: "))
    notas.append(no)
for k in range(4):
    for x in range(4-k):
        if(notas[x]<notas[x+1]):
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x]=aux2
print("La lista de alumnos y sus notas respectivas de mayor a menor")
for x in range(5):
    print(alumnos[x],notas[x])
