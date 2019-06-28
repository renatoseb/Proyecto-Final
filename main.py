from tkinter import *

raiz = Tk()

raiz.title('Comparador')
raiz.resizable(0,0)
raiz.geometry('750x400')
raiz.config(bg='gray')

abrircoleccion = Button(raiz, text="Abrir colección")
abrircoleccion.grid(column=2, row=0, padx=10, pady=10,sticky="w")

agregar= Button(raiz, text="Agregar más...")
agregar.grid(column=3, row=0 , pady=10)

listatxt = Listbox(raiz,height=20,width=28)
listatxt.grid(column=2, row=1, padx=10,columnspan=2,rowspan=2,sticky="w")
listatxt.insert(0,"Holakace")
listatxt.insert(1,"asdasf")
listatxt.insert(2,"sadasf")
listatxt.insert(3,"aeaeaeae")
listatxt.insert(4,"puctaaa")
listatxt.insert(5,"toyred")
listatxt.insert(6,"nosomobica")
listatxt.insert(7,"owowow")
listatxt.insert(8,"webiwebin")
listatxt.insert(9,"webiwebin")
listatxt.insert(10,"webiwebin")
listatxt.insert(11,"wefdsgsdfwebin")
listatxt.insert(12,"wegfdsgn")
listatxt.insert(13,"webihjfgjh")
listatxt.insert(14,"wgfadsdsfn")
listatxt.insert(15,"wdasfdsfn")
listatxt.insert(16,"webgfsgsadin")
listatxt.insert(17,"wegfdgsn")
listatxt.insert(18,"webiwebin")
listatxt.insert(19,"wegfdfgdn")
listatxt.insert(20,"webiwebin")
listatxt.insert(21,"weasdsadn")
listatxt.insert(22,"wesadsadn")
scrolvert=Scrollbar(raiz, command=listatxt.yview)
scrolvert.grid(row=2,column=4, sticky="nsew")
listatxt.config(yscrollcommand=scrolvert.set)


leerfigura= Button(raiz, text="Leer figura de consulta")
leerfigura.grid(column=5, row=0, sticky="w", padx=10 )
ventanamatriz= Listbox(raiz,height=20,width=35)
ventanamatriz.grid(column=5, row=2,padx=10,columnspan=2,rowspan=2)


ranking= Button(raiz, text="Ranking de Similitud")






raiz.mainloop()