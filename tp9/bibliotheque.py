class livre:
    titre: str
    nomAuteur: str
    anneeParution: int
    nbPages: int

menu_options = {
    1 : "Afficher l'ensemble des livres de la bibliothèque",
    2 : "Ajouter un nouveau livre",
    3 : "Rechercher un livre (par le titre)",
    4 : "Quitter"
}

def print_menu():
    for key in menu_options.keys():
        print(key, '-- ', menu_options[key])

def afficher_livres(table: list[livre],n:int):
    if n == 0:
        print("La bibliothèque est vide")
        return
    for livre in table:
        print("Titre: ", livre.titre)
        print("Auteur: ", livre.nomAuteur)
        print("Année de parution: ", livre.anneeParution)
        print("Nombre de pages: ", livre.nbPages)
        print("")  # Ligne vide pour séparer les livres

def ajouter_livre(table: list[livre], n:int):
    nouveau_livre = livre()
    nouveau_livre.titre = input("Entrez le titre du livre: ")
    nouveau_livre.nomAuteur = input("Entrez le nom de l'auteur: ")
    nouveau_livre.anneeParution = int(input("Entrez l'année de parution: "))
    nouveau_livre.nbPages = int(input("Entrez le nombre de pages: "))
    table.append(nouveau_livre)
    n+=1
    return n

def rechercher_livre(table: list[livre]):
    id:int
    titre = input("Entrez le titre du livre à rechercher: ")
    for id in range(len(table)):
        if table[id].titre == titre:
            print("Titre: ", table[id].titre)
            print("Auteur: ", table[id].nomAuteur)
            print("Année de parution: ", table[id].anneeParution)
            print("Nombre de pages: ", table[id].nbPages)
            return id
            

if __name__ == '__main__':
    table: list[livre] = []  # Déclaration du tableau
    n:int
    n=0
    place: int
    option = str      # Déclaration de la variable pour l'option choisie

    while True:
        print_menu()  # Affiche le menu
        option = ''
        try:
            option = input("Entrez votre choix: ")  # Lit le choix de l'utilisateur
        except:
            print("Entrez un nombre valide")

        if option == '1':
            afficher_livres(table,n)
        elif option == '2':
            n=ajouter_livre(table,n)
        elif option == '3':
            place=rechercher_livre(table)
            print("Le livre se trouve à la place ", place+1 )
            
        elif option == '4':
            break