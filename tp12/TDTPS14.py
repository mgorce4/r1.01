
from typing import Optional

# structure de maillon
class Maillon:
    data: int
    suivant: Optional["Maillon"]

# structure de liste
class ListeChainee:
    tete: Optional[Maillon]


def longueur(li: ListeChainee) -> int:
    """
    Fonction qui renvoie la longueur de la liste chainée
    entrée : li : ListeChainee
    sortie : int : longueur de la liste
    """
    courant = li.tete
    if courant:
        longueur = 1
        while(courant.suivant):
            longueur += 1
            courant = courant.suivant
        return longueur
    else:
        return 0
   

def afficheLC(li: ListeChainee):
    """Fonction qui affiche les éléments de la liste

    Dans cette version, chaque élément est affiché sur une ligne

    Args:
        li (ListeChainee): la liste que l'on veut afficher
    """
    courant = li.tete
    while(courant):
        print("|", end = "")
        print(courant.data , end = "|")
        courant = courant.suivant
    print("")


def ajoutQueue(li: ListeChainee, val: int):
    """
    fonction qui ajoute un élément en queue de liste chainée.

    """
    courant = li.tete
    if courant == None:
        li.tete = Maillon()
        li.tete.data = val
        li.tete.suivant = None
    else:
        while(courant.suivant):
            courant = courant.suivant
        courant.suivant = Maillon()
        courant.suivant.data = val
        courant.suivant.suivant = None


def ajoutTete(li: ListeChainee, val: int):
    """
    fonction qui ajoute un élément en tête de liste chainée
    """
    if li.tete == None:
        li.tete = Maillon()
        li.tete.data = val
        li.tete.suivant = None
    else:
        newMaillon = Maillon()
        newMaillon.data = val
        newMaillon.suivant = li.tete
        li.tete = newMaillon


def ajoutEnPos(li: ListeChainee, indice : int, val: int):
    """
    fonction qui ajoute un élément en position donnée de liste chainée
    """
    courant = li.tete
    if indice == 0:
        ajoutTete(li, val)
    else:
        for i in range(1, indice):
            if courant.suivant == None:
                print("Indice trop grand")
                return
            courant = courant.suivant
        newMaillon = Maillon()
        newMaillon.data = val
        newMaillon.suivant = courant.suivant
        courant.suivant = newMaillon

def suppTete(li : ListeChainee):
    """
    fonction qui supprime un élément en tête de liste chainée
    """
    if li.tete == None:
        print("Liste vide")
    else:
        li.tete = li.tete.suivant


def suppQueue(li : ListeChainee):
    """
    fonction qui supprime un élément en queue de liste chainée
    """
    courant = li.tete
    if courant == None:
        print("Liste vide")
    elif courant.suivant == None:
        li.tete = None
    else:
        while(courant.suivant.suivant):
            courant = courant.suivant
        courant.suivant = None


def suppEnPos(li: ListeChainee, indice : int):
    """
    fonction qui supprime un élément en position donnée de liste chainée
    """
    courant = li.tete
    if indice == 0:
        suppTete(li)
    else:
        for i in range(1, indice):
            if courant.suivant == None:
                print("Indice trop grand")
                return
            courant = courant.suivant
        if courant.suivant == None:
            print("Indice trop grand")
            return
        courant.suivant = courant.suivant.suivant


def recherche(li: ListeChainee, val : int) -> int :
    """
    fonction qui recherche un élément dans la liste chainée
    """
    courant = li.tete
    indice = 0
    while(courant):
        if courant.data == val:
            return indice
        courant = courant.suivant
        indice += 1
    return -1



if __name__=="__main__" :
    maLC = ListeChainee()
    maLC.tete = None
    # ecrire tous les tests / jeux d'essai
    # permettant de mettre en évidence le fonctionnement de la liste
    # ainsi que les cas particuliers (impossible de supprimer un élément 
    # d'une liste vide par exemple)

    afficheLC(maLC)
    ajoutTete(maLC, 0)
    afficheLC(maLC)
    ajoutTete(maLC, 1)
    afficheLC(maLC)
    ajoutTete(maLC, 2)
    afficheLC(maLC)
    ajoutQueue(maLC, 3)
    afficheLC(maLC)
    ajoutQueue(maLC, 4)
    afficheLC(maLC)
    ajoutEnPos(maLC, 2, 5)
    afficheLC(maLC)
    ajoutEnPos(maLC, 6, 7)
    afficheLC(maLC)
    suppTete(maLC)
    afficheLC(maLC)
    suppQueue(maLC)
    afficheLC(maLC)
    suppEnPos(maLC, 1)
    afficheLC(maLC)
    suppEnPos(maLC, 1)
    afficheLC(maLC)
    print(recherche(maLC, 2))
    print(recherche(maLC, 4))