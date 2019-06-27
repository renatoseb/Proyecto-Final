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



raiz.mainloop()
