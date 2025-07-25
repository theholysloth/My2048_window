IMPLEMENTATION 2048 EN CLI

Etape 1 : creation de la grille 
            la grille sera un tableau de 4*4 contenant des 0 en etat initiale 
            on fera apparaitre un nombre pseudo aleatoire (soit 2 soit 4 ) dans une case vide 
            chaque case de la grille sera definit par des | de part et d'autre. 
                si la case est vide alors plusieurs caractere espace
                sinon la valeur dans la grille

Etape 2 : Gestion des cases 
            les cases adjacentes de meme valeurs s'additionnent.
            les cases se deplacent dans la direction choisie
            une nouvelle case aparait tant qu'il y a au moins une case vide 
            on repete tant qu'une addition est possible
    procédé : 
        il parait complexe de decaler et additionner les cases en un seul temps.  nous allons donc le faire en deux temps : 
            decalage + addition. c-a-d decalage de toute les cases de sortes à combler les cases vides entre puis addition des cases ayant la meme valeur
        Pour le deplacement selon l'entrée du joueur, des fonctions adaptées à chacun des cas permettront de gereer le deplacement des cases
            move_left : c'est typiquement la fonction de decalage car on decale vers la gauche sauf que cette fois il faut penser à l'addition des cases de valeurs egales et surtout à retirer les cases vides ,entre les cases , apres les additions
            move_right : on utilisera la methode fliplr de numpy qui permet d'inverser les colonnes d'un tableau 2d (soit T=[1,2,3][4,5,6] np.fliplr(T)=[3,2,1][6,5,4]). on utilise cette methode à l'aide de move_left nous permettant de revenir à un etat correspondant à notre souhait 
                        illustration :  [0,0,0,0]               [0,0,0,0]                   [0,0,0,0]               [0,0,0,0]
                                        [0,4,0,2] =>fliplr =    [2,0,4,0] => move_left =    [0,0,2,4] => fliplr =   [4,2,0,0]
                                        [0,0,0,0]               [0,0,0,0]                   [0,0,0,0]               [0,0,0,0]
                                        [0,2,0,0]               [0,0,2,0]                   [0,0,0,2]               [2,0,0,0]
            move_up : un peu comme le proceder de move_right sauf qu'on utilisera cette fois la methode transpose() avec move_left dans les meme dispostion que fliplr . Transpose realise la transposé d'une matrice c-a-d il inverse les ligne et les colonnes: 
                    exp [1,2,3,4]       [1,5,6]
                        [5,4,8,9] =>    [2,4,0]
                        [6,0,0,0]       [3,8,0]
                                        [4,9,0]
            move_down :  pareil que move_up sauf qu'on utilise la methode transpose avec move_right

#deplacement dans le readme

Pour le jeu 
#rajouter un fichier de score
#rajouter une sauvegarde
#creation de session

Etape 3 : Fin de jeu 
            il n'y a fin de jeu que si les conditins suivantes sont remplies : 
                plus aucune case n'est vide
                plus aucune addition n'est possible (Horizontalement comme verticalement)