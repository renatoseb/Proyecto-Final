from tkinter import *
from os import scandir, getcwd
from os.path import abspath
from tkinter.font import Font
from tkinter import scrolledtext
from Funciones import *


rutafig="C:/ICC/PY3" #donde estaran las figuras
listanombre=nombresarchv(rutafig)
listaderutas=ruta(rutafig)
MIDICCIONARIO={}
nombres=nombresarchv(rutafig)
rutas=ruta(rutafig)
for x in range(len(listanombre)):
    MIDICCIONARIO[listanombre[x]]=busquedamatriz(listaderutas[x])
def abrir():
    global listabox
    listanombre=nombresarchv(rutafig)
    listaderutas=ruta(rutafig)
    listabox = Listbox(raiz,height=20,width=28)
    listabox.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")
    for x in range(len(listaderutas)):
        listabox.insert(x,listaderutas[x])

    scrolvert=Scrollbar(raiz, command=listabox.yview)
    scrolvert.grid(row=1,column=4, sticky="nsew")
    listabox.config(yscrollcommand=scrolvert.set)

def crear_ventana():
    global listaderutas
    global MIDICCIONARIO,valores,keys
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
        global listaderutas
        global MIDICCIONARIO,valores,keys
        #-------cambien en donde esta guardado su archivo--------
        file = open(rutafig+"/"+str(nombrenew.get())+".txt", "w")
        b="C:\\ICC\\PY3\\"+str(nombrenew.get())+".txt"
        listaderutas.append(b)
        for x in range(len(listanombre)):
            MIDICCIONARIO[listanombre[x]]=busquedamatriz(listaderutas[x])
        valores=list(MIDICCIONARIO.values())
        keys=list(MIDICCIONARIO.keys())
        #----aaaa---
        a=str(entradamatriz.get())
        file.write(a)
        window.destroy()

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
listabox = Listbox(raiz,height=20,width=28)
listabox.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")
abrircoleccion = Button(raiz, text="Abrir colección",command=abrir)
abrircoleccion.grid(column=2, row=0, padx=10, pady=10,sticky="w")

scrolvert=Scrollbar(raiz, command=listabox.yview)
scrolvert.grid(row=1,column=4, sticky="nsew")
listabox.config(yscrollcommand=scrolvert.set)
#=======


agregar= Button(raiz, text="Agregar más...", command=crear_ventana)
agregar.grid(column=3, row=0 , pady=10)
listanombre=nombresarchv(rutafig)
matriza=[]
#--------------Acá se mostrará la matriz a comparar impresa---------
def recuperar():
    global matriza,listaderutas
    valores=list(MIDICCIONARIO.values())
    ventanamatriz.delete(1.0,END)
    if len(listabox.curselection())!=0:
        w=listaderutas.index(listabox.get(listabox.curselection()[0]))
        matriza=valores[w]
        for x in matriza:
            for y in x:
                ventanamatriz.insert(END, str(y))
            ventanamatriz.insert(END, '\n')



leerfigura= Button(raiz, text="Leer figura de consulta",command=recuperar)
leerfigura.grid(column=5, row=0, sticky="w", padx=10 )

ventanamatriz= Text(raiz,width=28,height=20)
ventanamatriz.grid(column=5, row=1,padx=10,columnspan=2)






#---------- Ranking -------------
def rankinss():
    ventanaranking.delete(1.0,END)
    global matriza
    global MIDICCIONARIO
    valores=list(MIDICCIONARIO.values())
    keys=list(MIDICCIONARIO.keys())
    similitudes={}
    for x in range(len(valores)):
        similitudes[keys[x]]=similitud(matriza,valores[x])

##################

    listaparaquick=list(similitudes.values())
    listaordenada=quicksort(listaparaquick,0,len(listaparaquick)-1)
    demayoramenor=listaordenada[::-1]
    keysimilitudes=list(similitudes.keys())
    valoressiimiliud=list(similitudes.values())
    new={}
    for x in demayoramenor:
        a=valoressiimiliud.index(x)
        new[keysimilitudes[a]]=x
###################
    for x in new:
        ventanaranking.insert(END,str(x)+"\n")
        ventanaranking.insert(END,str(new[x])+"%"+"\n")
        for i in MIDICCIONARIO[x]:
            for j in i:
                ventanaranking.insert(END,str(j))
            ventanaranking.insert(END, '\n')
        ventanaranking.insert(END,'\n')


ranking= Button(raiz, text="Ranking de Similitud",command=rankinss)
ranking.grid(column=7, row= 0, sticky="w", padx=10)
ventanaranking= Text(raiz,width=30,height=20)
ventanaranking.grid(column=7, row=1, padx=10,columnspan=2)
scrolito=Scrollbar(raiz, command=ventanaranking.yview)
scrolito.grid(row=1,column=9, sticky="nsew")
ventanaranking.config(yscrollcommand=scrolito.set)


raiz.mainloop()



