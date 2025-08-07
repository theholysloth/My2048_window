import numpy as np
import json
import init
import gestion_case
import classement


def game_over(grille):
    if any(0 in row for row in grille):
        return False
    for i in range(4):
        for j in range(3):#verification de la possibilité d'additionner les cases
            if grille[i][j] == grille[i][j+1] or grille[j][i] == grille[j+1][i]:
                return False
    return True

def save_game(grille, score, player_name):
    game_data = {
        'grille': grille.tolist(),
        'score': int(score),
        'player_name': player_name
    }
    try:
        with open('save_game.json', 'r') as f:
            all_games = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_games = []

    # on remplace les données si le nom existe, sinon on ajoute
    updated = False
    for i, data in enumerate(all_games):
        if data['player_name'] == player_name:
            print(f"Partie de {player_name} trouvée, avec score {data['score']}. Voulez-vous la remplacer ? (O/N)")
            ##on affiche la grille??
            print("############################# Grille Trouvée : #############################\n")
            init.display_grille(np.array(data['grille']))
            print("#############################################################################\n")
            if input().strip().upper() == 'O':
                all_games[i] = game_data
                updated = True
                break
            else:
                print("Partie non sauvegardée.")
                return
    if not updated:
        all_games.append(game_data)

    with open('save_game.json', 'w') as f:
        json.dump(all_games, f)
    print("Partie sauvegardée avec succès !")

def load_game(player_name):
    try:
        with open('save_game.json', 'r') as f:
            game_data = json.load(f)
            for game in game_data:
                if game['player_name'] == player_name:
                    grille = np.array(game['grille'])
                    score = game['score']
                    print("Partie chargée avec succès !")
                    return grille, score
                else:
                    print("Aucune partie sauvegardée pour ce joueur.")
                    return None, 0
    except FileNotFoundError:
        print("Aucune partie sauvegardée trouvée.")
        return None, 0

def gameplay(grille=None, score=0 , player_name="PLAYER"):
    
    #grille = init.add_new_tile(grille)
    while not game_over(grille):
        print(f"score actuel : {score}")
        print("Votre grille actuelle : ")
        init.display_grille(grille)

        deplacement = input("Entrez la Lettre souhaitée pour le deplacement (G: gauche, B: bas, J: droite , Y: haut) ou SAVE pour sauver votre partie : ").strip().upper()
        grille_prec = grille.copy() #pour verifier si le joueur a effectué un mouvement

        if deplacement == "SAVE":
            save_game(grille, score, player_name)
            continue
        elif deplacement == "Y":
            grille, point_maj = gestion_case.move_up(grille)
            score += point_maj
        elif deplacement == "B":
            grille, point_maj= gestion_case.move_down(grille)
            score += point_maj
        elif deplacement == "G":
            grille, point_maj = gestion_case.move_left(grille)
            score += point_maj
        elif deplacement == "J":
            grille,point_maj = gestion_case.move_right(grille)
            score += point_maj

        else:
            print("Deplacement invalide invalide ! Veuillez reessayer avec une lettre valide")
            continue
        if not (np.array_equal(grille, grille_prec)):#s'il y a eu un mouvement
            grille = init.add_new_tile(grille)

    print("Game Over !")
    print(f"Votre score final est : {score}")
    save_game(grille, score, player_name)
    
    init.display_grille(grille)
    print("Pour voir les 10 meilleurs scores, tapez 'r'. Pour quitter, tapez 'q', Et n'importe quelle autre touche pour recommencer une partie.")
    while True:
        choice = input("Votre choix : ").strip().upper()
        if choice == 'R':
            classement.classement()
        elif choice == 'Q':
            print("Merci d'avoir joué !")
            break
        else:
            grille = init.init_game()
            score = 0
            grille = init.add_new_tile(grille)
            gameplay(grille, score, player_name)
            break


def play():
    print("Bienvenue dans le jeu 2048 made by theholysloth !")
    player_name = input("Entrez votre nom de joueur : ").strip().upper()
    choice = input("Voulez-vous (N)ouvelle partie ou (C)harger une partie ? ").strip().upper()

    if choice == 'N':
        grille = init.init_game()
        score = 0
        grille = init.add_new_tile(grille)
        gameplay(grille, score,player_name)
    elif choice == 'C':
        grille, score = load_game(player_name)
        if grille is not None:
            init.display_grille(grille)
            gameplay(grille, score)

        else:
            print("Aucune partie chargée.")
    else:
        print("Choix invalide. Veuillez recommencer.")

play()