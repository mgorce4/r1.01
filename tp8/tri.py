import time
import random

# Dictionnaire des options du menu, avec des descriptions pour chaque option
menu_options = {
    "1": "Créer un nouveau tableau de N cases (entre 0 et 100) remplies aléatoirement",
    "2": "Afficher le tableau de manière lisible",
    "3": "Trier le tableau (tri à bulle) et afficher le temps de traitement",
    "4": "Trier le tableau (tri par insertion) et afficher le temps de traitement",
    "5": "Rechercher un élément (dans le tableau trié)",
    "6": "Quitter"
}

# Fonction pour afficher le menu des options
def print_menu():
    for key in menu_options.keys():
        print(key, '-- ', menu_options[key])

# Fonction pour créer un tableau de taille n avec des entiers aléatoires entre 0 et 100
def create_table(n: int) -> list:
    table = []
    for i in range(n):
        table.append(random.randint(0, 100))
    return table

# Fonction pour afficher le tableau de manière lisible
def print_table(table: list[int]):
    for i in range(len(table)):
        print(table[i], end=' | ')
    print()

# Fonction de tri à bulle pour trier le tableau en place
# Le tri à bulle compare les éléments adjacents et les échange s'ils sont dans le mauvais ordre
def tri_a_bulle(table: list[int]) -> list:
    n = len(table)
    for i in range(n):
        for j in range(0, n - i - 1):
            if table[j] > table[j + 1]:
                table[j], table[j + 1] = table[j + 1], table[j]
    return table

# Fonction de tri par insertion pour trier le tableau en place
# Le tri par insertion prend chaque élément et l'insère dans la bonne position dans la partie triée du tableau
def tri_par_insertion(table: list[int]) -> list:
    n = len(table)
    for i in range(1, n):
        key = table[i]
        j = i - 1
        while j >= 0 and key < table[j]:
            table[j + 1] = table[j]
            j -= 1
        table[j + 1] = key
    return table

# Fonction de recherche dichotomique pour trouver un élément dans un tableau trié
# Elle renvoie l'index de l'élément si trouvé, sinon -1
def recherche_dichotomique(table: list[int], x: int) -> int:
    # Vérification si le tableau est trié, sinon retourne -1
    if table != sorted(table):
        print("Le tableau n'est pas trié.")
        return -1

    # Initialisation des indices de début et de fin
    n = len(table)
    debut = 0
    fin = n - 1

    # Recherche dichotomique, divisant l'intervalle en deux à chaque étape
    while debut <= fin:
        milieu = (debut + fin) // 2
        if table[milieu] == x:
            return milieu
        elif table[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

# Code principal, affichant le menu et gérant les choix de l'utilisateur
if __name__ == '__main__':
    table: list[int]  # Déclaration du tableau
    option = str      # Déclaration de la variable pour l'option choisie

    while True:
        print_menu()  # Affiche le menu
        option = ''
        try:
            option = input("Entrez votre choix: ")  # Lit le choix de l'utilisateur
        except:
            print("Entrez un nombre valide")
        
        # Gestion des options de menu
        if option == '1':
            # Option 1 : Crée un nouveau tableau
            n = int(input("Entrez le nombre de cases: "))
            table = create_table(n)
        elif option == '2':
            # Option 2 : Affiche le tableau actuel
            print_table(table)
        elif option == '3':
            # Option 3 : Trie le tableau avec le tri à bulle et mesure le temps de traitement
            start = time.time()
            table = tri_a_bulle(table)
            end = time.time()
            print_table(table)
            print("Temps de traitement: ", end - start)
        elif option == '4':
            # Option 4 : Trie le tableau avec le tri par insertion et mesure le temps de traitement
            start = time.time()
            table = tri_par_insertion(table)
            end = time.time()
            print_table(table)
            print("Temps de traitement: ", end - start)
        elif option == '5':
            # Option 5 : Recherche d'un élément dans le tableau trié
            x = int(input("Entrez l'élément à rechercher: "))
            index = recherche_dichotomique(table, x)
            if index != -1:
                print("L'élément est à l'index: ", index)
            else:
                print("L'élément n'est pas dans le tableau")
        elif option == '6':
            # Option 6 : Quitter le programme
            break
