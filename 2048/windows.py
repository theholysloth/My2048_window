import pygame
import numpy as np
import json
import init
import gestion_case
import classement
import sys

pygame.init()

largeur_fenetre = 700
hauteur_fenetre = 500
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("2048")


NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (200, 200, 200)
font = pygame.font.Font(None, 36)

couleurs = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

def afficher_texte_win(texte, position, couleur=NOIR):
    texte_surface = font.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(position))
    fenetre.blit(texte_surface, texte_rect)


def afficher_grille_win(grille):
    fenetre.fill((187, 173, 160))
    for i in range(4):
        for j in range(4):
            valeur = grille[i][j]
            couleur = couleurs[valeur] if valeur in couleurs else (60, 58, 50)
            pygame.draw.rect(fenetre, couleur, (j * 100 + 10, i * 100 + 10, 80, 80))
            if valeur != 0:
                texte = font.render(str(valeur), True, (119, 110, 101))
                texte_rect = texte.get_rect(center=(j * 100 + 50, i * 100 + 50))
                fenetre.blit(texte, texte_rect)
    #pygame.display.flip()

def get_input(prompt, y_position):# prompt ici est le texte à afficher
    max_length = 14  # Longueur maximale de l'entrée
    input_texte = ""
    largeur_rect = 200
    input_rect = pygame.Rect((largeur_fenetre - largeur_rect)//2, y_position, largeur_rect, 32)
    couleur_active = pygame.Color('lightskyblue3')
    couleur_inactive = pygame.Color('gray15')
    couleur = couleur_inactive
    actif = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    actif = True
                else:
                    actif = False
                couleur = couleur_active if actif else couleur_inactive
            if event.type == pygame.KEYDOWN:
                if actif:
                    if event.key == pygame.K_RETURN:
                        return input_texte
                    elif event.key == pygame.K_BACKSPACE:
                        input_texte = input_texte[:-1]
                    else:
                        if len(input_texte) < max_length:
                            if event.unicode.isprintable():
                                input_texte += event.unicode

        fenetre.fill(BLANC)
        afficher_texte_win(prompt, (largeur_fenetre //2, y_position - 30))
        pygame.draw.rect(fenetre, couleur, input_rect, 2)
        afficher_texte_win(input_texte, (input_rect.x + 100, input_rect.y +16))
        pygame.display.flip()


def bouton(fenetre, font , position, text = "Sauver") : 
    text_surface = font.render(text,True, NOIR)
    bouton_rect = pygame.Rect(position, (150,40))
    pygame.draw.rect(fenetre,(200,200,200), bouton_rect)
    pygame.draw.rect(fenetre, NOIR, bouton_rect, 2)# contour noir
    text_rect = text_surface.get_rect(center=bouton_rect.center) 
    fenetre.blit(text_surface, text_rect)
    return bouton_rect

