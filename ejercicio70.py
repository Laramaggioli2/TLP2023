paises=[]
habitantes=[]

for x in range(5):
    nom=input("Ingrese el nombre del país: ")
    paises.append(nom)
    no=int(input("Ingrese la cantidad de habitantes: "))
    habitantes.append(no)
for k in range(4):
    for x in range(4-k):
        if(habitantes[x]<habitantes[x+1]):
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x]=aux2
print("La lista de paises y su cantidad de habitantes respectiva de mayor a menor")
for x in range(5):
    print(paises[x],habitantes[x])
    
for z in range(4):
    for y in range(4-z):
        if(paises[y]>paises[y+1]):
            aux1=paises[y]
            paises[y]=paises[y+1]
            paises[y+1]=aux1
            aux2=paises[y]
            paises[y]=paises[y+1]
            paises[y]=aux2
print("La lista de paises alfabéticamente: ")
for x in range(5):
    print(paises[x])
