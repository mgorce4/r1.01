import time
import random
menu_options = {
    "1": "Créer un nouveau tableau de N cases (entre 0 et 100) remplies aléatoirement",
    "2": "Afficher le tableau de manière lisible" ,
    "3": "Trier le tableau (tri à bulle) et afficher le temps de traitement",
    "4": "Trier le tableau (tri par insertion) et afficher le temps de traitement",
    "5": "rechercher un élément (dans le tableau trié)",
    "6": "Quitter"
}

def print_menu():
    for key in menu_options.keys():
        print(key, '-- ', menu_options[key])

def create_table(n:int) -> list:
    table = []
    for i in range(n):
        table.append(random.randint(0, 100))
    return table

def print_table(table: list[int]):
    for i in range(len(table)):
        print(table[i], end=' | ')
    print()

def tri_a_bulle(table: list[int]) -> list:
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table[j] > table[j+1]:
                table[j], table[j+1] = table[j+1], table[j]
    return table

def tri_par_insertion(table: list[int]) -> list:
    n = len(table)
    for i in range(1, n):
        key = table[i]
        j = i-1
        while j >= 0 and key < table[j]:
            table[j+1] = table[j]
            j -= 1
        table[j+1] = key
    return table

def recherche_dichotomique(table: list[int], x: int) -> int:
    n = len(table)
    debut = 0
    fin = n-1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if table[milieu] == x:
            return milieu
        elif table[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

if __name__ == '__main__':
    table: list [int]
    option = str

    while (True):
        print_menu()
        option = ''
        try:
            option = input("Entrez votre choix: ")
        except:
            print("Entrez un nombre valide")
        
        if option == '1':
            n = int(input("Entrez le nombre de cases: "))
            table = create_table(n)
        elif option == '2':
            print_table(table)
        elif option == '3':
            start = time.time()
            table = tri_a_bulle(table)
            end = time.time()
            print_table(table)
            print("Temps de traitement: ", end-start)
        elif option == '4':
            start = time.time()
            table = tri_par_insertion(table)
            end = time.time()
            print_table(table)
            print("Temps de traitement: ", end-start)
        elif option == '5':
            x = int(input("Entrez l'élément à rechercher: "))
            index = recherche_dichotomique(table, x)
            if index != -1:
                print("L'élément est à l'index: ", index)
            else:
                print("L'élément n'est pas dans le tableau")
        elif option == '6':
            break