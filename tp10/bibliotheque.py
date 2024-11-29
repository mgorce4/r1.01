
class auteur:
    nom: str
    prenom: str
    nationalite: str
    dateNaissance: int
    dateDeces: int

class livre:
    titre: str
    author: auteur
    anneeParution: int
    nbPages: int


menu_options = {
    1 : "Afficher l'ensemble des livres de la bibliothèque",
    2 : "Ajouter un nouveau livre",
    3 : "Rechercher un livre (par le titre)",
    4 : "afficher les livres d'un auteur",
    5 : "ajouter un auteur",
    6 : "Quitter"
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
        print("Auteur: ", livre.author.nom)
        print("Année de parution: ", livre.anneeParution)
        print("Nombre de pages: ", livre.nbPages)
        print("-------------------------")  # Ligne vide pour séparer les livres

def ajouter_livre(table: list[livre], n:int, tableau_auteurs: list[auteur]):
    """
    fonction permettant d'ajouter un livre à la bibliothèque
    entrées: table(list[livre]) : tableau de livres, n(int) : nombre de livres dans la bibliothèque indenté de 1, tableau_auteurs(list[auteur]) : tableau d'auteurs
    sorties: n(int) : nombre de livres dans la bibliothèque indenté de 1
    """
    if len(tableau_auteurs) == 0:
        print("Aucun auteur disponible. Veuillez ajouter un auteur d'abord.")
        return n
    
    nouveau_livre = livre() # Création d'un nouveau livre
    nouveau_livre.titre = input("Entrez le titre du livre: ") 
    if len(tableau_auteurs) == 0:
        print("Aucun auteur disponible. Veuillez ajouter un auteur d'abord.")
        return n

    print("Liste des auteurs disponibles:")
    for idx, auteur in enumerate(tableau_auteurs):
        print(f"{idx + 1}. {auteur.nom} {auteur.prenom}")

    choix_auteur = int(input("Choisissez un auteur par son numéro: ")) - 1
    if choix_auteur < 0 or choix_auteur >= len(tableau_auteurs):
        print("Choix invalide.")
        return n

    nouveau_livre.author = tableau_auteurs[choix_auteur]
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
            print("Auteur: ", table[id].author.nom)
            print("Année de parution: ", table[id].anneeParution)
            print("Nombre de pages: ", table[id].nbPages)
            print("-------------------------")
            return id
    return -1  # Si le livre n'est pas trouvé, retourne -1
            
def ajout_auteur (tableau_auteurs: list[auteur], n:int):
    """
    fonction permettant d'ajouter un auteur à la bibliothèque
    entrées: tableau_auteurs(list[auteur]) : tableau d'auteurs, n(int) : nombre d'auteurs dans la bibliothèque
    sorties: n(int) : nombre d'auteurs dans la bibliothèque indenté de 1
    """
    nouvel_auteur = auteur() # Création d'un nouvel auteur
    nouvel_auteur.nom = input("Entrez le nom de l'auteur: ")
    nouvel_auteur.prenom = input("Entrez le prénom de l'auteur: ")
    nouvel_auteur.nationalite = input("Entrez la nationalité de l'auteur: ")
    nouvel_auteur.dateNaissance = int(input("Entrez l'annee de naissance de l'auteur: "))
    nouvel_auteur.dateDeces = int(input("Entrez l'annee de décès de l'auteur: "))
    tableau_auteurs.append(nouvel_auteur) # Ajout de l'auteur au tableau
    n+=1 # Incrémentation du nombre d'auteurs
    return n

def livres_d_un_auteur(table: list[livre], tableau_auteurs: list[auteur]):
    """
    procédure permettant d'afficher les livres d'un auteur
    entrées: table(list[livre]) : tableau de livres, tableau_auteurs(list[auteur]) : tableau d'auteurs
    sorties: aucune
    """
    if len(table) == 0: # Si le tableau est vide on affiche un message
        print("La bibliothèque est vide")
        return
    if len(tableau_auteurs) == 0: # Si le tableau d'auteurs est vide on affiche un message
        print("Aucun auteur disponible")
        return
    print("Liste des auteurs disponibles:")
    for idx, auteur in enumerate(tableau_auteurs):
        print(f"{idx + 1}. {auteur.nom} {auteur.prenom}")
    choix_auteur = int(input("Choisissez un auteur par son numéro: ")) - 1
    if choix_auteur < 0 or choix_auteur >= len(tableau_auteurs):
        print("Choix invalide.")
        return
    auteur = tableau_auteurs[choix_auteur]
    print(f"Livres de {auteur.nom} {auteur.prenom}:")
    for livre in table:
        if livre.author == auteur:
            print(f"Titre: {livre.titre}")
            print(f"Année de parution: {livre.anneeParution}")
            print(f"Nombre de pages: {livre.nbPages}")
            print("-------------------------")

if __name__ == '__main__':
    table: list[livre] = []  # Déclaration du tableau
    tableau_auteurs: list[auteur] = []
    n:int
    n_auteur:int
    n_auteur=0
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
            n=ajouter_livre(table,n,tableau_auteurs) 
        elif option == '3':
            place=rechercher_livre(table)
            if place == -1:
                print("Le livre n'est pas dans la bibliothèque")
            elif place == -2:
                pass
            else:
                print("Le livre se trouve à la place ", place+1 )
        
        elif option == '4':
            livres_d_un_auteur(table,tableau_auteurs)

        elif option == '5':
            n_auteur=ajout_auteur(tableau_auteurs,n_auteur)

        elif option == '6':
            break