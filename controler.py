from constante import *


def Clic(event):
    """ Gestion de l'événement Clic gauche """
    global DETECTION_CLIC_SUR_OBJET

    canvas = event.widget

    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    item = canvas.find_closest(x, y)

    # position du pointeur de la souris
    X = event.x
    Y = event.y
    print("Position du clic -> ", X, Y)
    print(canevas.coords(item[0]))
    # coordonnées de l'objet
    [xmin, ymin] = canevas.coords(item[0])

    print("Position objet -> ", xmin, ymin)
    if xmin <= X and ymin <= Y:
        DETECTION_CLIC_SUR_OBJET = True
    else:
        DETECTION_CLIC_SUR_OBJET = False
    print("DETECTION CLIC SUR OBJET -> ", DETECTION_CLIC_SUR_OBJET)


def Drag(event):
    """ Gestion de l'événement bouton gauche enfoncé """
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    item = canvas.find_closest(x, y)
    print(item)

    X = event.x
    Y = event.y
    print("Position du pointeur -> ", X, Y)

    if DETECTION_CLIC_SUR_OBJET == True:
        # limite de l'objet dans la zone graphique
        if X < 0:
            X = 0
        if X > SCREEN_WIDTH:
            X = SCREEN_WIDTH
        if Y < 0:
            Y = 0
        if Y > SCREEN_HEIGHT:
            Y = SCREEN_HEIGHT
        # mise à jour de la position de l'objet (drag)
        canevas.coords(item, X-HauteurI, Y-HauteurI)


def convertStrToInt(L):
    T = []
    for i in L:
        T.append(int(i))
    return T


def verfier_somme():
    pass


def createBoard(canevas, x, y, img):
    return canevas.create_image(x, y, image=Photoimage(img))


def createLabelAndAnswer(fen, color, x_pos, y_pos):
    choix2 = Label(fen, text="10", fg="white", bg=color,
                   font=("Helvetica", 14), height=2, width=3)

    choix2.place(x=x_pos, y=y_pos)
    choixNum1 = canevas.create_text(
        SCREEN_WIDTH - 50, 220, text="4", fill="#616060",
        font="Times 18 bold")


def getChiffrePic(chemin):
    return PhotoImage(file=chemin)


def recommencer_jeu():
    all_chiffre = []
    game_completed = False


def getChiffreValue(id):
    return chiffre[id]["value"]


def createChiffre(canevas, x, y, image):
    return canevas.create_image(x, y, anchor=NW, image=image)


def getChiffreId():
    return chiffre[id]


def getChiffreCoord():
    return chiffre[id]["coord"]


def get_level_in_file(niveau='facile'):
    """
    Principe de génération des parties on récupérera ces données dans un fichier txt qu'on va créer
    """
    t = "niveau/{}.txt".format(niveau)
    f = open(t, "r")
    levels = []
    with open(t, "r") as f:
        seps = f.readlines()
        for x in seps:
            sep = x.strip("\n").split("|")
            i = int(sep[0])
            nombre_a_trouver = convertStrToInt(sep[1].split(","))
            reponse = convertStrToInt(sep[2].split(","))
            level = [i, nombre_a_trouver, reponse]
            levels.append(level)

    return levels


print(get_level_in_file('difficile'))
