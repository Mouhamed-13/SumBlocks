from tkinter import *
from constante import *
from random import randrange, sample
from tkinter.messagebox import *


# crÃ©ation de la fenetre
fen = Tk()
fen.title("SUM Blocks")
fen.iconbitmap("assets/deplacer.ico")
# fen.background("#D6ABAB")


# crÃ©ation du canevas
canevas = Canvas(fen, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="#D6ABAB")

image1 = PhotoImage(file="assets/7.png")
image2 = PhotoImage(file="assets/3.png")
image3 = PhotoImage(file="assets/1.png")
rect1 = PhotoImage(file="assets/bleu.png")
rect2 = PhotoImage(file="assets/rose.png")

R1 = canevas.create_image(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, image=rect1)
R2 = canevas.create_image(SCREEN_WIDTH // 2 + 50,
                          SCREEN_HEIGHT // 2 + 50, image=rect2)
ima1 = canevas.create_image(50, 120, anchor=NW, image=image1)
ima2 = canevas.create_image(50, 230, anchor=NW, image=image2)
ima3 = canevas.create_image(50, 340, anchor=NW, image=image3)

choix1 = Label(fen, text="4", fg="white", bg="pink",
               font=("Helvetica", 14), height=2, width=3)
choix2 = Label(fen, text="10", fg="white", bg="blue",
               font=("Helvetica", 14), height=2, width=3)
choix1.place(x=SCREEN_WIDTH - 100, y=200)
choix2.place(x=SCREEN_WIDTH - 100, y=300)
choixNum1 = canevas.create_text(
    SCREEN_WIDTH - 50, 220, text="4", fill="#616060",
    font="Times 18 bold")
choixNum2 = canevas.create_text(
    SCREEN_WIDTH - 50, 320, text="10", fill="#616060",
    font="Times 18 bold")
print(canevas.find_all())
title = canevas.create_text(
    SCREEN_WIDTH // 2, 30, text="SUM Blocks", fill="#616060",
    font="Times 37 bold")
level = canevas.create_text(
    SCREEN_WIDTH // 2, 80, text="1/30", fill="white",
    font="Times 32 bold")


canevas.focus_set()
canevas.pack(padx=10, pady=10)

bou1 = Button(fen, text='Solveur')
bou1.pack(side=LEFT, padx=0, pady=20)
bou2 = Button(fen, text='Recommencer')
bou2.pack(side=BOTTOM, padx=0, pady=0)
bou3 = Button(fen, text='Retour')
bou3.pack(side=RIGHT, padx=20, pady=0)

fen.mainloop()

# main()
