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
    """
    Affiche le menu des options
    entrées: aucune
    sorties: aucune
    """
    for key in menu_options.keys():
        print(key, '-- ', menu_options[key])

def afficher_livres(table: list[livre],n:int):
    """
    procédure permettant d'afficher les livres de la bibliothèque de livres renvoie un message d'eereur si le tableau est vide
    entrées: table(list[livre]) : tableau de livres, n(int) : nombre de livres dans la bibliothèque
    sorties: aucune
    """
    if n == 0: # Si le tableau est vide on affiche un message
        print("La bibliothèque est vide")
        return
    for livre in table: # Parcours le tableau et affiche les livres
        print("Titre: ", livre.titre)
        print("Auteur: ", livre.nomAuteur)
        print("Année de parution: ", livre.anneeParution)
        print("Nombre de pages: ", livre.nbPages)
        print("-------------------------")  # Ligne vide pour séparer les livres

def ajouter_livre(table: list[livre], n:int):
    """
    fonction permettant d'ajouter un livre à la bibliothèque
    entrées: table(list[livre]) : tableau de livres, n(int) : nombre de livres dans la bibliothèque
    sorties: n(int) : nombre de livres dans la bibliothèque indenté de 1
    """
    nouveau_livre = livre() # Création d'un nouveau livre
    nouveau_livre.titre = input("Entrez le titre du livre: ") 
    nouveau_livre.nomAuteur = input("Entrez le nom de l'auteur: ")
    nouveau_livre.anneeParution = int(input("Entrez l'année de parution: "))
    nouveau_livre.nbPages = int(input("Entrez le nombre de pages: "))
    table.append(nouveau_livre) # Ajout du livre au tableau
    n+=1 # Incrémentation du nombre de livres
    return n

def rechercher_livre(table: list[livre]):
    """
    fonction permettant de rechercher un livre dans la bibliothèque par son titre
    entrées: table(list[livre]) : tableau de livres
    sorties: id(int) : position du livre dans le tableau
    """
    if len(table) == 0: # Si le tableau est vide on affiche un message
        print("La bibliothèque est vide")
        return -2
    titre = input("Entrez le titre du livre à rechercher: ") # Demande le titre du livre à rechercher
    for id in range(len(table)): # Parcours le tableau
        if table[id].titre == titre: # Si le titre du livre est trouvé on affiche le livre
            print("Titre: ", table[id].titre)
            print("Auteur: ", table[id].nomAuteur)
            print("Année de parution: ", table[id].anneeParution)
            print("Nombre de pages: ", table[id].nbPages)
            print("-------------------------")
            return id
    return -1  # Si le livre n'est pas trouvé, retourne -1
            

if __name__ == '__main__':
    table: list[livre] = []  # Déclaration du tableau
    n:int
    n=0
    place: int
    option = str # Déclaration de la variable pour l'option choisie

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
            if place == -1:
                print("Le livre n'est pas dans la bibliothèque")
            elif place == -2:
                pass
            else:
                print("Le livre se trouve à la place ", place+1 )
            
        elif option == '4':
            break