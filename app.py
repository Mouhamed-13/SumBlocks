from tkinter import *
from controler import *
from constante import *
from random import randrange, sample
from tkinter.messagebox import *


def game():
    global imageDepart, game_started

    canevas.delete(imageQuit)
    canevas.delete(imageHelp)
    canevas.delete(imageSetting)
    canevas.delete(imageStart)
    game_started = True


def clic(event):
    global game_started
    if not game_started:
        game()


def aide(event):
    showinfo(title="Aide", message=AIDE)


def about(event):
    showinfo(title="A propos", message=ABOUT)


def clicDestroy(event):
    fen.destroy()


# crÃ©ation de la fenetre
fen = Tk()
fen.title("SUM Blocks")

# crÃ©ation du canevas
canevas = Canvas(fen, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="#D6ABAB")

canevas.pack()
startImg = PhotoImage(file="assets/jouer.png")
helpImg = PhotoImage(file="assets/aide.png")
settingImg = PhotoImage(file="assets/parametre.png")
quitImg = PhotoImage(file="assets/quitter.png")
warningImg = PhotoImage(file="assets/warning.png")
title = canevas.create_text(
    SCREEN_WIDTH // 2, 60, text="SUM Blocks", fill="#616060",
    font="Times 42 bold")
imageStart = canevas.create_image(
    SCREEN_WIDTH // 2, SCREEN_WIDTH // 6, image=startImg)
imageHelp = canevas.create_image(
    SCREEN_WIDTH // 2, SCREEN_WIDTH // 4, image=helpImg)
imageSetting = canevas.create_image(
    SCREEN_WIDTH // 2, SCREEN_WIDTH // 3, image=settingImg)
imageQuit = canevas.create_image(
    SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 190, image=quitImg)
imageWarning = canevas.create_image(
    SCREEN_WIDTH-28, SCREEN_HEIGHT-28, image=warningImg)

print(canevas.find_all())
#fen.bind("<Button>", clic)
canevas.tag_bind(imageStart, '<Button-1>', clic)
canevas.tag_bind(imageQuit, '<Button-1>', clicDestroy)
canevas.tag_bind(imageHelp, '<Button-1>', aide)
canevas.tag_bind(imageWarning, '<Button-1>', about)

fen.mainloop()

# main()
