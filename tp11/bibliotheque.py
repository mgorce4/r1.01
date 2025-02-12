import pickle

def write_list(table: list, filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(table, file)

def read_list(filename: str) -> list:
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

class auteur:
    nom: str
    prenom: str
    nationalite: str
    dateNaissance: int
    dateDecesFacultative: str

class livre:
    titre: str
    author: auteur
    anneeParution: int
    nbPages: int

menu_options = {
    1 : "Afficher l'ensemble des livres de la bibliothèque",
    2 : "Ajouter un nouveau livre",
    3 : "Rechercher un livre (par le titre)",
    4 : "Afficher les livres d'un auteur",
    5 : "Ajouter un auteur",
    6 : "Afficher tous les auteurs", 
    7 : "exporter les données au format texte",
    8 : "exporter les données au format CSV",
    9 : "importer les données depuis un fichier texte",
    10 : "importer les données depuis un fichier CSV",
    11 : "Quitter"
}

def print_menu():
    for key in menu_options.keys():
        print(key, '-- ', menu_options[key])

def afficher_livres():
    table = read_list('livres.pkl')
    if len(table) == 0:
        print("La bibliothèque est vide")
        return
    for livre in table:
        print("Titre: ", livre.titre)
        print("Auteur: ", livre.author.nom)
        print("Année de parution: ", livre.anneeParution)
        print("Nombre de pages: ", livre.nbPages)
        print("-------------------------")

def ajouter_livre():
    table : []
    table = read_list('livres.pkl')
    tableau_auteurs = read_list('auteurs.pkl')
    if len(tableau_auteurs) == 0:
        print("Aucun auteur disponible. Veuillez ajouter un auteur d'abord.")
        return
    
    nouveau_livre = livre()
    nouveau_livre.titre = input("Entrez le titre du livre: ")
    print("Liste des auteurs disponibles:")
    for idx, auteur in enumerate(tableau_auteurs):
        print(f"{idx + 1}. {auteur.nom} {auteur.prenom}")

    choix_auteur = int(input("Choisissez un auteur par son numéro: ")) - 1
    if choix_auteur < 0 or choix_auteur >= len(tableau_auteurs):
        print("Choix invalide.")
        return

    nouveau_livre.author = tableau_auteurs[choix_auteur]
    nouveau_livre.anneeParution = int(input("Entrez l'année de parution: "))
    nouveau_livre.nbPages = int(input("Entrez le nombre de pages: "))
    table.append(nouveau_livre)
    write_list(table, 'livres.pkl')

def rechercher_livre():
    table = read_list('livres.pkl')
    if len(table) == 0:
        print("La bibliothèque est vide")
        return -2
    titre = input("Entrez le titre du livre à rechercher: ")
    for id in range(len(table)):
        if table[id].titre == titre:
            print("Titre: ", table[id].titre)
            print("Auteur: ", table[id].author.nom)
            print("Année de parution: ", table[id].anneeParution)
            print("Nombre de pages: ", table[id].nbPages)
            print("-------------------------")
            return id
    return -1

def ajout_auteur():
    tableau_auteurs = []
    tableau_auteurs = read_list('auteurs.pkl')
    nouvel_auteur = auteur()
    nouvel_auteur.nom = input("Entrez le nom de l'auteur: ")
    nouvel_auteur.prenom = input("Entrez le prénom de l'auteur: ")
    nouvel_auteur.nationalite = input("Entrez la nationalité de l'auteur: ")
    nouvel_auteur.dateNaissance = int(input("Entrez l'année de naissance de l'auteur: "))
    nouvel_auteur.dateDecesFacultative = input("Entrez l'année de décès de l'auteur (facultatif): ")
    tableau_auteurs.append(nouvel_auteur)
    write_list(tableau_auteurs, 'auteurs.pkl')

def livres_d_un_auteur():
    table = read_list('livres.pkl')
    tableau_auteurs = read_list('auteurs.pkl')
    if len(table) == 0:
        print("La bibliothèque est vide")
        return
    if len(tableau_auteurs) == 0:
        print("Aucun auteur disponible")
        return
    print("Liste des auteurs disponibles:")
    for idx, auteur in enumerate(tableau_auteurs):
        print(f"{idx + 1}. {auteur.nom} {auteur.prenom}")
    choix_auteur = int(input("Choisissez un auteur par son numéro: ")) - 1
    while choix_auteur < 0 or choix_auteur >= len(tableau_auteurs):
        print("Choix invalide.")
    auteur = tableau_auteurs[choix_auteur]
    print(f"Livres de {auteur.nom} {auteur.prenom}:")
    for livre in table:
        if livre.author == auteur:
            print(f"Titre: {livre.titre}")
            print(f"Année de parution: {livre.anneeParution}")
            print(f"Nombre de pages: {livre.nbPages}")
            print("-------------------------")

def tousLesAuteurs():
    tableau_auteurs = read_list('auteurs.pkl')
    if len(tableau_auteurs) == 0:
        print("Aucun auteur disponible")
        return
    for auteur in tableau_auteurs:
        print("Nom: ", auteur.nom)
        print("Prénom: ", auteur.prenom)
        print("Nationalité: ", auteur.nationalite)
        print("Année de naissance: ", auteur.dateNaissance)
        print("Année de décès: ", auteur.dateDecesFacultative)
        print("-------------------------")

def exporter_au_format_texte():
    table = read_list('livres.pkl')
    if len(table) == 0:
        print("La bibliothèque est vide")
        return
    with open('bibliotheque.txt', 'w') as file:
        for livre in table:
            file.write(f"Titre: {livre.titre}\n")
            file.write(f"Auteur: {livre.author.nom} {livre.author.prenom}\n")
            file.write(f"Année de parution: {livre.anneeParution}\n")
            file.write(f"Nombre de pages: {livre.nbPages}\n")
            file.write("-------------------------\n")

def exporter_au_format_csv():
    table = read_list('livres.pkl')
    if len(table) == 0:
        print("La bibliothèque est vide")
        return
    with open('bibliotheque.csv', 'w') as file:
        file.write("Titre,Auteur,Année de parution,Nombre de pages\n")
        for livre in table:
            file.write(f"{livre.titre},{livre.author.nom} {livre.author.prenom},{livre.anneeParution},{livre.nbPages}\n")

def importer_du_format_texte():
    table = []
    with open('bibliotheque.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            livre = livre()
            livre.titre = lines[i].split(': ')[1].strip()
            auteur = lines[i + 1].split(': ')[1].strip().split(' ')
            livre.author.nom = auteur[0]
            livre.author.prenom = auteur[1]
            livre.anneeParution = int(lines[i + 2].split(': ')[1].strip())
            livre.nbPages = int(lines[i + 3].split(': ')[1].strip())
            table.append(livre)
    write_list(table, 'livres.pkl')

def importer_du_format_csv():
    table = []
    with open('bibliotheque.csv', 'r') as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
            livre = livre()
            data = lines[i].split(',')
            livre.titre = data[0]
            auteur = data[1].split(' ')
            livre.author.nom = auteur[0]
            livre.author.prenom = auteur[1]
            livre.anneeParution = int(data[2])
            livre.nbPages = int(data[3])
            table.append(livre)
    write_list(table, 'livres.pkl')



if __name__ == '__main__':
    while True:
        print_menu()
        option = input("Entrez votre choix: ")
        if option == '1':
            afficher_livres()
        elif option == '2':
            ajouter_livre()
        elif option == '3':
            place = rechercher_livre()
            if place == -1:
                print("Le livre n'est pas dans la bibliothèque")
            elif place == -2:
                pass
            else:
                print("Le livre se trouve à la place ", place + 1)
        elif option == '4':
            livres_d_un_auteur()
        elif option == '5':
            ajout_auteur()
        elif option == '6':
            tousLesAuteurs()
        elif option == '7':
            exporter_au_format_texte()
        elif option == '8':
            exporter_au_format_csv()
        elif option == '9':
            importer_du_format_texte()
        elif option == '10':
            importer_du_format_csv()
        elif option == '11':
            break