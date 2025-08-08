import numpy as np
import random

def init_game() : 
    # 4x4 matrix with all zeros
    grille = np.zeros((4,4), dtype=int)
    return grille 

def add_new_tile(grille) : 
    cellule_vide = [(i,j) for i in range(4) for j in range(4) if grille[i][j] == 0] #repertorie les celulles vides
    if cellule_vide:
        (l, c)  = random.choice(cellule_vide)
        grille[l][c] = random.choice([2,4]) #parmis les cellules vides , choisir une et y mettre 2 ou 4
    return grille

def display_grille(grille) : 
    print("-"*25)
    for c in grille : 
        print("|", end = " ")
        for v in c : 
            if v == 0 : 
                print(" "*4, end = " | ")
            else : 
                print(f"{v:4d}", end = " | ")
        print()
        print("-"*25)

