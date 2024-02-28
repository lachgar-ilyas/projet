import random

def Grille(grille):
    for row in grille:
        print("|".join(row))
        print("-" * 5)

def Victoire(grille, joueur):
    for row in grille:
        if all(cell == joueur for cell in row):
            return True

    for col in range(3):
        if all(row[col] == joueur for row in grille):
            return True

    if all(grille[i][i] == joueur for i in range(3)) or \
       all(grille[i][2-i] == joueur for i in range(3)):
        return True

    return False

def jouer():
    while True:
        grille = [[" " for _ in range(3)] for _ in range(3)]
        joueurs = ['X', 'O']
        tour = 0

        while True:
            joueur = joueurs[tour % 2]
            if joueur == 'X':  # Joueur humain
                Grille(grille)
                while True:
                    try:
                        row = int(input("Entrez le numéro de ligne entre 0 et 2: "))
                        col = int(input("Entrez le numéro de colonne entre 0 et 2: "))
                        if 0 <= row < 3 and 0 <= col < 3 and grille[row][col] == " ":
                            break
                        else:
                            print("Position invalide. Réessayez.")
                    except ValueError:
                        print("Entrez un nombre valide.")
            else:  # IA
                row, col = choisir_coup(grille, joueur)

            grille[row][col] = joueur

            if Victoire(grille, joueur):
                Grille(grille)
                if joueur == 'X':
                    print("Vous avez gagné !")
                else:
                    print("HAHAHA Vous avez perdu !")
                break

            if all(cell != " " for row in grille for cell in row):
                Grille(grille)
                print("Match nul !")
                break

            tour += 1

        rejouer = input("Voulez-vous rejouer ? (Y/N) ").strip().lower()
        if rejouer != 'oui':
            print("Au revoir !")
            break

def choisir_coup(grille, joueur):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = joueur
                if Victoire(grille, joueur):
                    return i, j
                else:
                    grille[i][j] = " "

    adversaire = 'X' if joueur == 'O' else 'O'
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = adversaire
                if Victoire(grille, adversaire):
                    grille[i][j] = joueur
                    return i, j
                else:
                    grille[i][j] = " "

    cases_vides = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == ' ']
    return random.choice(cases_vides)

jouer()
