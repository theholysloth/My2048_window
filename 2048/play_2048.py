import numpy as np
import json
import init
import gestion_case
import classement
import pygame
import windows
import sys



pygame.init()

largeur_fenetre = 400
hauteur_fenetre = 500
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("2048")

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (200, 200, 200)
font = pygame.font.Font(None, 36)


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
    
    running = True
    input_active = False
    input_text = ""

    while not game_over(grille) or running:
        fenetre.fill(BLANC)
        windows.afficher_texte_win(f"score actuel : {score}",(10, 10))
        windows.afficher_texte_win("Votre grille actuelle : ",(10,50))
        windows.afficher_grille_win(grille)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                grille_prec = grille.copy()  # pour vérifier si le joueur a effectué un mouvement

                if not input_active:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT:
                        grille, point_maj = gestion_case.move_left(grille)
                        score += point_maj
                    elif event.key == pygame.K_RIGHT:
                        grille, point_maj = gestion_case.move_right(grille)
                        score += point_maj
                    elif event.key == pygame.K_UP:
                        grille, point_maj = gestion_case.move_up(grille)
                        score += point_maj
                    elif event.key == pygame.K_DOWN:
                        grille, point_maj = gestion_case.move_down(grille)
                        score += point_maj
                    elif event.key == pygame.K_s:  # pour sauvegarder
                        save_game(grille, score, player_name)
                else:
                    if event.key == pygame.K_ESCAPE: 
                        if input_text == "SAVE" : 
                            save_game(grille, score, player_name)
                        input_active = False
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

                if not np.array_equal(grille, grille_prec):  
                    grille = init.add_new_tile(grille)
    
    fenetre.fill(BLANC)
    windows.afficher_texte_win("Game Over !", (largeur_fenetre // 2 - 50, hauteur_fenetre // 2 - 50), NOIR)
    windows.afficher_texte_win(f"Votre score final est : {score}", (largeur_fenetre // 2 - 100, hauteur_fenetre // 2), NOIR)
    windows.afficher_texte_win("Appuyez sur 'R' pour voir le classement, 'Q' pour quitter, ou n'importe quelle autre touche pour recommencer.", (10, hauteur_fenetre // 2 + 50))
    pygame.display.flip()

    save_game(grille, score, player_name)
    windows.afficher_grille_win(grille)

    attente_choix = True
    while attente_choix:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    classement.classement()
                    attente_choix = False
                elif event.key == pygame.K_q:
                    windows.afficher_texte_win("Merci d'avoir joué !", (largeur_fenetre // 2 - 100, hauteur_fenetre // 2 + 100))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    pygame.quit()
                    sys.exit()
                else:
                    grille = init.init_game()
                    score = 0
                    grille = init.add_new_tile(grille)
                    gameplay(grille, score, player_name)
                    attente_choix = False

def play():

    fenetre.fill(BLANC)
    windows.afficher_texte_win("Entrer votre nom de joueur :", (80,50))
    pygame.display.flip()
    player_name = windows.get_input("Entrez votre nom de joueur : ",80).strip().upper()

    fenetre.fill(BLANC)
    windows.afficher_texte_win("Voulez-vous (N)ouvelle partie ou (C)harger une partie ? ",(50,120))
    pygame.display.flip()
    choice = windows.get_input("N pour Nouvelle partie, C pour Charger une partie : ",150).strip().upper()

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
            fenetre.fill(BLANC)
            windows.afficher_texte_win("Aucune partie trouvée pour ce joueur.", (50, 200))
            pygame.display.flip()
            pygame.time.wait(2000)
            grille = init.init_game()
            score = 0
            grille = init.add_new_tile(grille)
            gameplay(grille, score,player_name)
    else:
        fenetre.fill(BLANC)
        windows.afficher_texte_win("Choix invalide. Veuillez recommencer.", (50, 200))
        pygame.display.flip()
        pygame.time.wait(2000)
        play()  # relance la fonction pour recommencer le jeu

if __name__ == "__main__":
    init.init_game()  # Initialisation de la grille
    print("############################# Bienvenue dans 2048 made by theholysloth ! #############################\n")
    play()
    print("#######################################################################################################\n")
    pygame.quit()