import random
essais = 10
lifes = essais

def get_word(niveau):
    # Le dictionnaire(apparemment un dico doit avoir une unicité dans ses clés, du coup j'ai inversé key & value)
    dico_a = {
        "lait": 1,
        "pour": 1,
        "flamme": 2,
        "positif": 2,
        "terminaison": 3,
        "allumette": 3
    }
    # Création d'un nouveau dictionnaire contenant uniquement des clés et valeurs,
    # pour lesquelles la valeur est égale au niveau choisi par le joueur
    dico_b = {}
    for key, value in dico_a.items():
        if value == int(niveau):
            dico_b[key] = value
    # choix d'un mot du dico grace à la méthode random
    mot = random.choice(list(dico_b.keys()))
    return mot


def display(lettre,terme,evolution):
    longueur = len(terme)
    liste = list(terme)
    traits = []

    if evolution == "":
        for x in range(longueur):
            traits.append("_")
        print(traits)
    else:
        traits = list(evolution)
        lettre = input("Entrez votre lettre:\n")

    ultimo = match_word(liste,lettre,traits,terme)
    print(ultimo)
    return ultimo


def match_word(suite, caractere, evo, chaine):
    global lifes
    #fonction de vérification des conditions suivantes:
    # nombre de tentatives restantes
    # la lettre proposée est-elle dans le mot?
    bad_letter="Lettre proposée non incluse dans le mot!"
    v = 0
    if caractere in suite:
        for x in suite:
            if caractere == x:
                print(v)
                evo[v] = caractere
            v += 1
    else:
        print(bad_letter)
        lifes -= 1
    print(lifes)
    print(evo, list(chaine))
    # renvoi d'une valeur "win", "lose" ou "les lettres actuellement découvertes"
    if evo == list(chaine):
        end = "win"
        return end
    elif lifes == 0:
        end = "lose"
        return end
    else:
        end = ''.join(evo)
        return end


def print_menu():
    welcome_message = "---Bienvenue sur le Jeu du pendu!---"
    difficulty = "Veuillez choisir votre niveau de difficulté!\n 1:Easy \n 2:Normal \n 3:Hard \n q:Quit \n"
    winner = "Bravo vous avez remporté la victoire et découvert le mot x en x tentatives"
    loser = "Désolé de cet échec, le mot à découvrir était : x"
    again = "Souhaitez-vous refaire une partie? (O)ui ou (N)on \n"
    deviner = "Veuillez entrer une première lettre\n"
    bye = "Au revoir!"

    print(welcome_message)
    level = input(difficulty) # Demander au joueur de choisir le level de difficulté


    ### Appel de la Function -> get_word()
    if level not in 'qQ':
        fin = ""
        ### Appel de la fonction get_word avec paramétre level
        word = get_word(level)
        #print("Le mot c'est:", word)
        ### Appel de la Function -> display()
        letter = input(deviner)
        fin = display(letter, word, fin)
        print(fin)

        while not (fin == "win") and not (fin == "lose"):
            fin = display(letter, word, fin)
        if fin == "win":
            print(winner)
        elif fin == "lose":
            print(loser)
    else:
        print(bye)
        exit()


    stop_or_continue = input(again) # Demander au joueur s'il veux rejouer ou quitter

    if stop_or_continue in 'oO':
        global lifes
        global essais
        lifes = essais
        print_menu()
    elif stop_or_continue in 'nN':
        print(bye)
        exit()# Sortie du programme
