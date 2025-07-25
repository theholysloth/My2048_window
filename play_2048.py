import numpy as np
import init
import gestion_case


def game_over(grille):
    if any(0 in row for row in grille):
        return False
    for i in range(4):
        for j in range(3):#verification de la possibilité d'additionner les cases
            if grille[i][j] == grille[i][j+1] or grille[j][i] == grille[j+1][i]:
                return False
    return True

def play():
    grille = init.init_game()
    grille = init.add_new_tile(grille)
    while not game_over(grille):
        print("Votre grille actuelle : ")
        init.display_grille(grille)
        deplacement = input("Entrez la Lettre souhaitée pour le deplacement (G: gauche, B: bas, J: droite , Y: haut) : ").strip().upper()
        grille_prec = grille.copy() #pour verifier si le joueur a effectué un mouvement

        if deplacement == "Y":
            grille = gestion_case.move_up(grille)
        elif deplacement == "B":
            grille = gestion_case.move_down(grille)
        elif deplacement == "G":
            grille = gestion_case.move_left(grille)
        elif deplacement == "J":
            grille = gestion_case.move_right(grille)
        else:
            print("Deplacement invalide invalide ! Veuillez reessayer avec une lettre valide")
            continue
        if not (np.array_equal(grille, grille_prec)):#s'il y a eu un mouvement
            grille = init.add_new_tile(grille)

    print("Game Over !")
    init.display_grille(grille)



play()