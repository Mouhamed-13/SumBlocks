import pygame
from pygame.locals import *
pygame.init()

# Déclarations de tous les sons
erreur_song = pygame.mixer.Sound("sons/echoue.wav")
success_song = pygame.mixer.Sound("sons/reussie.wav")
quit_song = pygame.mixer.Sound("sons/quit.wav")


""" Liste Des Constantes liées à l'affichage"""
SCREEN_HEIGHT, SCREEN_WIDTH = 610, 1180
NB_CASES = 4
ONE_CASE_WIDTH = SCREEN_WIDTH/NB_CASES
SUCCESS_COLOR = '#ff8700'
game_started = False
DETECTION_CLIC_SUR_OBJET = False

HauteurI = 25
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# garde tous les chiffres générés
chiffre = {
    # 'id': {"image": path, "value": nombre, "coord": (x, y)}
}

# id des chiffres générés
all_chiffre = []


# Va contenir nos chiffres générés ainsi si on déplace un chiffre sa position dans la liste sera à None
cases = [None, None, None, None]

# Vérifie si tous les chiffres posés dans les cases correpondent aux nombres recherchés
game_completed = True

AIDE = "Ce jeu à réflexion mathématiques consiste à calculer des sommes en utilisant des blocs de numéros requis qui seront additionnés pour résoudre le problème et obtenir la bonne combinaison du chiffre ou du nombre requis. Déplacer les blocs de numéro et choisissez où les placer dans le jeu sur les carrés en couleur pour atteindre vos objectifs et passer au niveau suivant. Utilisez le solveur si vous êtes coincés.Bonne chance et bonne partie de jeu !"
ABOUT = "Jeu réalisé par Attitkpati-Dickel-Mouhamed Diop !!"
