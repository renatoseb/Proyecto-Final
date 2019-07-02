from os import scandir, getcwd
from os.path import abspath

def partition(A,low,high):
    i = low 
    pivot = A[low]
    for j in range(low + 1,high + 1):
        if A[j] <= pivot:
            i +=1
            if i != j:
                A[i] , A[j] = A[j] , A[i]
    A[i] , A[low] = A[low] , A[i]
    w = i
    return w
def quicksort(A,low,high):
    if low < high:
        w = partition(A,low,high)
        quicksort(A,low,w-1)
        quicksort(A,w+1,high)
    return A
def filascolumnas(n): # n = una matriz, esta funcion para retornar el numero de filas y columnas
  fiyco=[] # lista vacía
  fila=0
  columna=0
  for i in n:
    fila+=1 # se cuenta los elementos, que son las filas
    columna=len(i) # como las listas dentre de la lista grande tienen igual numero de elementos, la columna no varía
  fiyco.append(fila)
  fiyco.append(columna)
  return fiyco  # retorna las filas y columnas de una matriz (en una lista)

def totalceldas(n): # n es una matriz
  total=0 # contador
  for j in n: # va por fila
    for i in j: # va por dentre de la fila, las columnas
      total+=1
  return total  # retorna el total de elementos de la matriz

def similitud(n,b): # n,b son matrices
  fica_n=filascolumnas(n) # fica son filas y columnas de n y b
  fica_b=filascolumnas(b)
  if fica_b!=fica_n:
    return 0 # cuando no son iguales en filas o columnas

  else:
    a=0
    c=0
    cont=0
    total_celdas_n=totalceldas(n) # total de elementos en n, no se condiciona porque n y b tienen los mismos elementos
    for i in range(total_celdas_n):
      if n[a][c]==b[a][c]:
        cont+=1
      c+=1
      if c==len(n[0]): # se iguala al primer elemento
        c=0
        a+=1

    similitudn_b=cont/total_celdas_n  # el cont brindara el numero total de elementos iguales y se divide entre el total para averiguar cuanto se parece

    porcentaje=round(similitudn_b*100,2) # se multiplica por 100 para el porcentaje y se redondea

    return porcentaje

def nombresarchv(ruta = getcwd()):
    b= [arch.name for arch in scandir(ruta) if arch.is_file()]
    for x in range(len(b)):
        b[x]=b[x].rstrip(".txt")
    return b
def ruta(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
def busquedamatriz(Filename):
  a=open(Filename)  # se abre el archivo con la matriz dentro (ES LA RUTA)

  mimatriz=a.read()  # se asigna esa matriz a una variable (pero aun no esta en lista de listas)

  b=mimatriz.split("\n") # se divide por el salto de linea
  ma=[] # será la matriz
  for x in b: # "b" ya esta en lista de listas, pero sus elementos no
    c=list(x)
    ma.append(c) # se añade a una nueva lista
  return ma  # retorna el archivo en una matriz(listas dentro de otra lista)


