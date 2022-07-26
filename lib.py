import random
def get_word(niveau):
    # Le dictionnaire(apperemment un dico doit avoir une unicité dans ses clés, du coup j'ai inversé key & value)
    dico = {
        "lait": 1,
        "pour": 1,
        "flamme": 2,
        "positif": 2,
        "terminaison": 3,
        "allumette": 3
    }
    # Création d'un nouveau dictionnaire contenant uniquement des clés et valeurs,
    # pour lesquelles la valeur est égale au niveau choisi par le joueur
    d = {}
    for key, value in dico.items():
        if value == int(niveau):
            d[key] = value
    #print(d)
    # choix d'un mot du dico grace à la méthode random
    #print(niveau)
    #print(random.choice(list(d.keys())))
    mot = random.choice(list(d.keys()))
    return mot


def display(lettre,terme):
    end = ""
    tour = ""
    longueur = len(terme)

    liste = list(terme)
    soluce3 = []

    for x in range(longueur):
        soluce3.append("_")
    print(soluce3)

    v = 0
    for x in liste:

        if lettre == x:
            print(v)
            soluce3[v] = lettre
        v += 1
    print(soluce3)
    # renvoi d'une valeur "win", "lose" ou "les lettres actuellement découvertes"
    if soluce3 == terme:
        end = "win"
        return end
    elif tour == 0:
        end = "lose"
        return end
    else:
        end = ''.join(soluce3)
        return end


"""
def dico(letter, word):
    {

    }

"""
def print_menu():
    word=""
    fin=""
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
        word = get_word(level)
        print("Le mot c'est:", word)
        ### Appel de la Function -> display()
        letter = input("Entre ta lettre\n")
        fin = display(letter,word)
        print(fin)
        """if fin == "win":
            print("Bravo")
        elif fin == "lose":
            print("loser")
        else:"""
            ######A finir fin = display(letter, word)
    else:
        print("No Game!")
        exit()


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
