retry = False

while not retry:
    nbr = int(input("Veuillez saisir un nombre : "))
    print(nbr)

    for i in range(11):
        print(nbr * i)

    choice = input("Voullez vous recommencer? (Y/N) ").lower()

    if choice == "Y":
        retry = False
    elif choice == "N":
        retry = True
        print("FIN")
    else:
        print("Choix invalide. Recommencez!")
        print("1")
