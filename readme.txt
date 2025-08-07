IMPLEMENTATION 2048 EN CLI

Etape 1 : creation de la grille 
            la grille sera un tableau de 4*4 contenant des 0 en etat initial
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

Etape 3 : score 
            initialemnt le score est à 0. Il evoluera en fonction des tuiles additionnées, c'est à dire si on additionne deux cases ayant la valeur 2 , on ajoute 2+2 donc 4 au score ; cc'est pareil pour 4 , 8, 16, ...
            L'objectif est d'associer une session à un score .

Etape 4 : sauvegarde et chargement
            L'idee ici est de sauver le score, l'etat de la grille au moment de la sauvegarde et le nom du joueur. Ainsi il sera possible de sauvegarder une partie, de reprendre le cours de celle ci lorsque voulu sans rien perdre.
            On souhaite utiliser des données JSON pour cela . les données seront de type 
            {
                nom : string
                grille : array[4][4]
                score : int 
                mot de passe : string (mot de passe chiffré et optionnel pour le moment)
            }
            ###On rajoute un mdp pour eviter que 2 joueurs du meme nom confondent leurs sauvegarde et aussi pour eviter une usurpation de partie.

            Avant de sauvegarder une partie pour un joueur , ca serait bien de prevenir s'il a une partie deja dans la BD 

Pour le jeu 
#rajouter un classement  : 
    le classement utilisera les donnée JSON, la logiqe serait de comparer et classer les score de la facon la plus intuitive possible
#rajouter une sauvegarde : done 
#creation de session : à moitié
#rajouter un moyen simple de quitter le jeu 

Etape 3 : Fin de jeu 
            il n'y a fin de jeu que si les conditins suivantes sont remplies : 
                plus aucune case n'est vide
                plus aucune addition n'est possible (Horizontalement comme verticalement)