from tkinter import *
def crear_ventana():
    window = Toplevel(raiz)
    window.geometry("300x300")
    window.title("Nueva matriz")
    milabel=Label(window,text="Ingrese nueva matriz")
    milabel.pack()
    entradamatriz=Entry(window)
    entradamatriz.pack(fill=X , ipady=50)
def abrir():
    listatxt = Listbox(raiz,height=20,width=28)
    listatxt.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")
    for x in range(1,k+1):
        listatxt.insert(x-1,"figura"+str(x)+".txt")

    scrolvert=Scrollbar(raiz, command=listatxt.yview)
    scrolvert.grid(row=1,column=4, sticky="nsew")
    listatxt.config(yscrollcommand=scrolvert.set)

#def leercoleccion():
k=20
raiz = Tk()

raiz.title('Comparador')
raiz.resizable(0,0)
raiz.geometry('840x460')
raiz.config(bg='gray')
raiz.config(bd=35)
raiz.config(relief="sunken")

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
