from carre import Carre
from tkinter import * 

fenetre = Tk()

Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE, bg='red')
Frame1.pack(side=LEFT, padx=300, pady=300)



#monCarre = Carre()
#msg = monCarre.couleur

#label = Label(fenetre, text=msg)
#label.pack()

fenetre.mainloop()