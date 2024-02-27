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
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ['X', 'O']
    tour = 0

    while True:
        joueur = joueurs[tour % 2]
        print(f"C'est au tour du joueur {joueur}")

        Grille(grille)

        while True:
            try:
                row = int(input("Entrez le numéro de ligne entre 0 et 2: "))
                col = int(input("Entrez le numéro de colonne entre 0 et 2"))
                if 0 <= row < 3 and 0 <= col < 3 and grille[row][col] == " ":
                    break
                else:
                    print("Position invalide. Réessayez.")
            except ValueError:
                print("Entrez un nombre valide.")

        grille[row][col] = joueur

        if Victoire(grille, joueur):
            Grille(grille)
            print(f"Le joueur {joueur} a gagné !")
            break

        if all(cell != " " for row in grille for cell in row):
            Grille(grille)
            print("Match nul !")
            break

        tour += 1

jouer()
