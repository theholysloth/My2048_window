import numpy as np 
import init

def decalage(grille): 
    grille_temp = np.zeros((4,4), dtype=int)

    for i in range(4):
        decal = 0 
        for j in range(4): 
            if grille[i][j] != 0 : #si la case n'est pas vide
                grille_temp[i][decal] = grille[i][j] #on decale les valeurs non vides à gauche histoire de retirer celles=0
                decal += 1 #va permettre derapprocher le cases avec valeurs differentes de 0 
    return grille_temp

def addition(grille): 
    points = 0 #initialisation du nombre de point gagné en un mouvement
    for i in range(4): 
        for j in range(3): 
            if grille[i][j] == grille[i][j+1] and grille[i][j] != 0 : #si 2 cases adjacentes sont identiques et non vides
                grille[i][j] = 2*grille[i][j] #on les additionne
                points += grille[i][j] #on ajoute le score
                grille[i][j+1] = 0 #on met la case de droite à 0
    return grille , points


def move_left(grille): 
    grille = decalage(grille)
    grille, points_tour = addition(grille)
    grille = decalage(grille)
    return grille, points_tour

def move_right(grille):
    grille = np.fliplr(grille)
    grille, points_tour = move_left(grille)
    grille = np.fliplr(grille)
    return grille, points_tour

def move_up(grille):
    grille = np.transpose(grille)
    grille,points_tour = move_left(grille)
    grille = np.transpose(grille)
    return grille, points_tour

def move_down(grille):
    grille = np.transpose(grille)
    grille,points_tour = move_right(grille)
    grille = np.transpose(grille)
    return grille, points_tour