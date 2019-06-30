from tkinter import *
from os import scandir, getcwd
from os.path import abspath

def rutas(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def nombresarchivos(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]


rutafig="C:/ICC/PY3" #donde estaran las figuras


def abrir():
    listanombre=nombresarchivos(rutafig)
    listaderutas=nombresarchivos(rutafig)
    listatxt = Listbox(raiz,height=20,width=28)
    listatxt.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")
    for x in range(len(listaderutas)):
        listatxt.insert(x,listaderutas[x])

    scrolvert=Scrollbar(raiz, command=listatxt.yview)
    scrolvert.grid(row=1,column=4, sticky="nsew")
    listatxt.config(yscrollcommand=scrolvert.set)
def crear_ventana():
    window = Toplevel(raiz)
    window.geometry("300x300")
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
    we= Button(window, text="Agregar",command=agregar)
    we.pack(side=BOTTOM, padx=5, pady=5)
#def leercoleccion():

raiz = Tk()

raiz.title('Comparador')
raiz.resizable(0,0)
raiz.geometry('840x460')
raiz.config(bg='gray')
raiz.config(bd=35)
raiz.config(relief="sunken")
var=StringVar()

#-------------Parte de los archivos------------

abrircoleccion = Button(raiz, text="Abrir colección",command=abrir)
abrircoleccion.grid(column=2, row=0, padx=10, pady=10,sticky="w")
listatxt = Listbox(raiz,height=20,width=28)
listatxt.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")


agregar= Button(raiz, text="Agregar más...", command=crear_ventana)
agregar.grid(column=3, row=0 , pady=10)



#--------------Acá se mostrará la matriz a comparar impresa---------

leerfigura= Button(raiz, text="Leer figura de consulta")
leerfigura.grid(column=5, row=0, sticky="w", padx=10 )
ventanamatriz= Listbox(raiz,width=35)
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


