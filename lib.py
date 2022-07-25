"""def get_word(level):
    {

    }


def display(word):
    {

    }


def dico(letter, word):
    {

    }

"""
def print_menu():
    word=""


    dico = {}
    welcome_message = "Bienvenue sur le jeu du pendu!"
    difficulty = "Veuillez choisir votre niveau de difficulté!\n 1:Easy \n 2:Normal \n 3:Hard \n q:Quit \n"
    win = "Bravo vous avez remporté la victoire et découvert le mot x en x tentatives"
    fail = "Désolé de cet échec, le mot à découvrir était : x"
    again = "Souhaitez-vous refaire une partie? (O)ui ou (N)on \n"
    deviner = "Veuillez entre une lettre"
    lettre = ""
    print(welcome_message)
    level = input(difficulty) # Demander au joueur de choisir le level de difficulté
    #print(level)


    ### Appel de la Function -> get_word()
    if level not in 'qQ':
        ###word=get_word(level) # Appel de la fonction get_word avec paramétre level
        print("Go Game!")
    else:
        print("No Game!")
        exit()

    ### Appel de la Function -> display()
    ###display(word) # Lancement du jeu sur le à deviner
    """lettre = input(deviner)

    def la_lettre
    if len(lettre) == 1:
        print("The letter is", lettre)
    else:
        print("No Game!")
    """
    ### Appel de la Function -> dico()


    stop_continue = input(again) # Demander au joueur s'il veux rejouer ou quitter

    if stop_continue in 'oO':
        print_menu()
    elif stop_continue in 'nN':
        print("Adieu")
        exit()# Sortie du programme
