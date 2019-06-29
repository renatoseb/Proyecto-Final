from tkinter import *
from tkinter import scrolledtext

raiz = Tk()

raiz.title('Comparador')
raiz.resizable(0,0)
raiz.geometry('800x400')
raiz.config(bg='gray')


#-------------Parte de los archivos------------

abrircoleccion = Button(raiz, text="Abrir colección")
abrircoleccion.grid(column=2, row=0, padx=10, pady=10,sticky="w")

agregar= Button(raiz, text="Agregar más...")
agregar.grid(column=3, row=0 , pady=10)

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



#--------------Acá se mostrará la matriz a comparar impresa---------

leerfigura= Button(raiz, text="Leer figura de consulta")
leerfigura.grid(column=5, row=0, sticky="w", padx=10 )
ventanamatriz= scrolledtext.ScrolledText(raiz,width=28,height=20)
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
