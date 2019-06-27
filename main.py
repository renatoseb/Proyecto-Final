from tkinter import *

raiz = Tk()

raiz.title('Comparador')
raiz.resizable(0,0)
raiz.geometry('900x500')
raiz.config(bg='gray')

abrircoleccion = Button(raiz, text="Abrir colección")
abrircoleccion.grid(column=1, row=0, padx=10, pady=20)

agregar= Button(raiz, text="Agregar más...")
agregar.grid(column=2, row=0 , pady=10)

listatxt = Listbox(raiz)
listatxt.grid(column=1, row=3, columnspan=2, padx=10)
listatxt.insert(0,"Holakace")

raiz.mainloop()
