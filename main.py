from tkinter import *

from tkinter import scrolledtext

from os import scandir, getcwd
from os.path import abspath

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
rutafig="C:/ICC/PY3" #donde estaran las figuras
listanombre=nombresarchv(rutafig)
listaderutas=ruta(rutafig)
MIDICCIONARIO={}
nombres=nombresarchv(rutafig)
rutas=ruta(rutafig)
for x in range(len(listanombre)):
    MIDICCIONARIO[listanombre[x]]=busquedamatriz(listaderutas[x])

def abrir():
    listanombre=nombresarchv(rutafig)
    listaderutas=ruta(rutafig)
    listatxt = Listbox(raiz,height=20,width=28)
    listatxt.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")
    for x in range(len(listaderutas)):
        listatxt.insert(x,listaderutas[x])

    scrolvert=Scrollbar(raiz, command=listatxt.yview)
    scrolvert.grid(row=1,column=4, sticky="nsew")
    listatxt.config(yscrollcommand=scrolvert.set)
def crear_ventana():
    global MIDICCIONARIO
    window = Toplevel(raiz)
    window.geometry("300x300+500+300")
    window.resizable(0,0)
    window.config(bg="grey")
    window.title("Nueva matriz")
    milabel=Label(window,text="Ingrese nueva matriz")
    milabel.pack()
    entradamatriz=Entry(window)
    entradamatriz.pack(fill=X , ipady=50)
    Label(window,text="Ingrese nombre de la matriz").pack(ipady=5)
    nombrenew=Entry(window)
    nombrenew.pack(fill=X,pady=30)
    def agregar():
        k=21
        #-------cambien en donde esta guardado su archivo--------
        file = open(rutafig+"/"+str(nombrenew.get())+".txt", "w")
        k+=1
        #----aaaa---
        a=str(entradamatriz.get())
        file.write(a)
        window.destroy()
    matrisss=str(entradamatriz.get()).split("\n")
    newmatriz=[]
    for x in matrisss:
        c=list(x)
        newmatriz.append(c)
    MIDICCIONARIO[nombrenew.get()]=newmatriz
    we= Button(window, text="Agregar",command=agregar)
    we.pack(side=BOTTOM, padx=5, pady=5)
#def leercoleccion():


raiz = Tk()

raiz.title('Comparador')
raiz.resizable(0,0)
#<<<<<<< HEAD
raiz.geometry('800x400')
#=======
raiz.geometry('840x460+500+300')

raiz.config(bg='gray')
raiz.config(bd=35)
raiz.config(relief="sunken")
var=StringVar()

#-------------Parte de los archivos------------

abrircoleccion = Button(raiz, text="Abrir colección",command=abrir)
abrircoleccion.grid(column=2, row=0, padx=10, pady=10,sticky="w")
listatxt = Listbox(raiz,height=20,width=28)
listatxt.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")

listatxt.insert(0,"Figura1.txt")
listatxt.insert(1,"Figura2.txt")
listatxt.insert(2,"Figura3.txt")
listatxt.insert(3,"Figura4.txt")
listatxt.insert(4,"Figura5.txt")
listatxt.insert(5,"Figura6.txt")
listatxt.insert(6,"Figura7.txt")
listatxt.insert(7,"Figura8.txt")
listatxt.insert(8,"Figura9.txt")
listatxt.insert(9,"Figura10.txt")
listatxt.insert(10,"Figura11.txt")
listatxt.insert(11,"Figura12.txt")
listatxt.insert(12,"Figura13.txt")
listatxt.insert(13,"Figura14.txt")
listatxt.insert(14,"Figura15.txt")
listatxt.insert(15,"Figura16.txt")
listatxt.insert(16,"Figura17.txt")
listatxt.insert(17,"Figura18.txt")
listatxt.insert(18,"Figura20.txt")

scrolvert=Scrollbar(raiz, command=listatxt.yview)
scrolvert.grid(row=1,column=4, sticky="nsew")
listatxt.config(yscrollcommand=scrolvert.set)
#=======


agregar= Button(raiz, text="Agregar más...", command=crear_ventana)
agregar.grid(column=3, row=0 , pady=10)




#--------------Acá se mostrará la matriz a comparar impresa---------

leerfigura= Button(raiz, text="Leer figura de consulta")
leerfigura.grid(column=5, row=0, sticky="w", padx=10 )
ventanamatriz= Label(raiz,width=28,height=20)
ventanamatriz.grid(column=5, row=1,padx=10,columnspan=2)


 



#---------- Ranking -------------


ranking= Button(raiz, text="Ranking de Similitud")
ranking.grid(column=7, row= 0, sticky="w", padx=10)
ventanaranking= Listbox(raiz,width=45,height=20) 
ventanaranking.grid(column=7, row=1, padx=10, columnspan=2)
scrolito=Scrollbar(raiz, command=ventanaranking.yview)
scrolito.grid(row=1,column=9, sticky="nsew")
ventanaranking.config(yscrollcommand=scrolito.set)


raiz.mainloop()


