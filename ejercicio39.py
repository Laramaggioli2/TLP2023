puntos=int(input("Ingrese una cantidad de puntos: "))
for i in range (puntos) :
     x=int(input("Ingrese una coordenada x : "))
     y=int(input("Ingrese otra coordenada y: "))
     if x>0 and y>0 :
         print("Pertenece al cuadrante 1")
     else:
         if x<0 and y>0:
             print("Pertenece al cuadrante 2")
         else:
             if x<0 and y<0:
                 print("Pertenece al cuadrante 3")
             else:
                 if x>0 and y<0:
                     print("Pertenece al cuadrante 4")
      
