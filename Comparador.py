# +--------------------+
# |           +----+   |
# |   +-------+    |   |
# |   |       |    |   |
# |   +-------+    |   |
# |           +----+   |
# +--------------------+

fila1 = []
fila2 = []
fila3 = []
fila4 = []
fila5 = []
fila6 = []
fila7 = []
 
for i in "+--------------------+":
    fila1.append(i)
for i in "|           +----+   |":
    fila2.append(i)
for i in "|   +-------+    |   |":
    fila3.append(i)
for i in "|   |       |    |   |":
    fila4.append(i)
for i in "|   +-------+    |   |":
    fila5.append(i)
for i in "|           +----+   |":
    fila6.append(i)
for i in "+--------------------+":
    fila7.append(i)
 
figura1 = [fila1,fila2,fila3,fila4,fila5,fila6,fila7]


# *--------------------*
# |           *----*   |
# |   *-------*    |   |
# |   |       |    |   |
# |   *-------*    |   |
# |           *----*   |
# *--------------------*
 
fila1 = []
fila2 = []
fila3 = []
fila4 = []
fila5 = []
fila6 = []
fila7 = []
 
for i in "*--------------------*":
    fila1.append(i)
for i in "|           *----*   |":
    fila2.append(i)
for i in "|   *-------*    |   |":
    fila3.append(i)
for i in "|   |       |    |   |":
    fila4.append(i)
for i in "|   *-------*    |   |":
    fila5.append(i)
for i in "|           *----*   |":
    fila6.append(i)
for i in "*--------------------*":
    fila7.append(i)
 
figura2 = [fila1,fila2,fila3,fila4,fila5,fila6,fila7]

def fs(figure,original):
    vueltas=0
    acum=0
    cont=0
    cont_fila=0
    for fila in figure:
        for i in fila:
            print(i, end='')
        print()
    for fila in original:
        for i in fila:
            print(i, end='')
        print('')
    if len(figure[0])==len(original[0]) and len(figure)==len(original):
        for fila in figure:
            for i in fila:
                if i==original[cont_fila][cont]:
                    acum+=1
                vueltas+=1
                cont+=1
            cont=0
            cont_fila+=1
        print('Numero de caracteres:',vueltas)
        print('Numero de caracteres iguales:',acum)
        
        porcentaje=acum/vueltas
        
        if porcentaje==1:
            print('La copia es idéntica de la original')
        elif porcentaje>=0.8:
            print("La copia es parcialmente identica con", round(100*(acum/vueltas)), "% de similitud")
        else:
            print("La copia difiere de la original.", round(100*(acum/vueltas)), "% de similitud")
    else:
        print("No se pueden comparar las figuras")

#imagen1
for fila in figura1:
    for i in fila:
        print(i, end='')
    print()
    

#imagen2
for fila in figura2:
    for i in fila:
        print(i, end='')
    print()

x=1

while x==1:
    
    input1=int(input('Primera imagen: '))
    input2=int(input('Segunda imagen: '))
    
    imagen1=''
    imagen2=''
    
    if input1==1:
        imagen1= figura1
    elif input1==2:
        imagen1= figura2
    else:
        imagen1=0
        
    if input2==1:
        imagen2= figura1
    elif input2==2:
        imagen2= figura2
    else:
        imagen2=0
    
    
    if imagen1==0 and imagen2==0:
        print('Seleccione imagenes validas')
    elif imagen1==0:
        print('Primera imagen invalida')
    elif imagen2==0:
        print('Segunda imagen invalida')
    else:
        fs(imagen1,imagen2)
    
    x= int(input("Desea comparar más imágenes? \n 1 = Si \n 0 = No \n"))
