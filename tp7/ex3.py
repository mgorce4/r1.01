menu_options = {
    "1": "Saisir un tableau de noms",
    "2": "Afficher le nombre de voyelles par nom",
    "3": "Afficher uniquement les noms étant des palindromes",
    "4": "Quitter",
}

def print_menu():
    for key in menu_options.keys():
        print(key, '- -', menu_options[key])

def compte_voyelles(chaine):
    voyelles = {'a', 'e', 'i', 'o', 'u', 'y','é','è','ê','à','ù','â','î','ô','û'}
    nb_voyelles = 0
    for lettre in chaine:
        if lettre in voyelles:
            nb_voyelles += 1
    return nb_voyelles

def est_palindrome(mot):
    for i in range(len(mot) // 2):
        if mot[i] != mot[len(mot) - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    noms = []

    while True:
        print_menu()
        option = input("Choix : ")

        if option == '1':
            # Saisie d'un tableau de noms
            while True:
                nom = input("Entrez un nom : ")
                noms.append(nom)
                continuer = input("Encore un nom ? (o/n) : ")
                if continuer.lower() == 'o':
                    continue
                if continuer.lower() == 'n':
                    break
                while continuer.lower() != 'o' or 'n':
                    continuer = input("Encore un nom ? (o/n) : ")
                


        elif option == '2':
            # Afficher le nombre de voyelles par nom
            for nom in noms:
                nb_voyelles = compte_voyelles(nom)
                print(f"Nombre de voyelles dans '{nom}' : {nb_voyelles}")

        elif option == '3':
            # Afficher les noms qui sont des palindromes
            print("Noms étant des palindromes :")
            palindromes = [nom for nom in noms if est_palindrome(nom)]
            if palindromes:
                for palindrome in palindromes:
                    print(palindrome)
            else:
                print("Aucun palindrome trouvé.")

        elif option == '4':
            print("Au revoir!")
            break

        else:
            print("Option invalide, veuillez réessayer.")
