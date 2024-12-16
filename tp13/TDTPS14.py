
from typing import Optional

# structure de maillon
class Maillon:
    def __init__(self, data: int = 0, suivant: Optional["Maillon"] = None, precedent: Optional["Maillon"] = None):
        self.data = data
        self.suivant = suivant
        self.precedent = precedent

# structure de liste
class ListeChainee:
    def __init__(self):
        self.tete: Optional[Maillon] = None

# liste d'entiers doublement chainée
class ListeDoubleChainee:
    def __init__(self):
        self.tete: Optional[Maillon] = None
        self.queue: Optional[Maillon] = None


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

def longueurDoublementChainee(li: ListeDoubleChainee) -> int:
    """
    Fonction qui renvoie la longueur de la liste doublement chainée
    entrée : li : ListeDoubleChainee
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
    print("|", end = "")
    while(courant):
        print(courant.data , end = "|")
        courant = courant.suivant
    print("")

def afficheListeDoubleChainee(li: ListeDoubleChainee):
    """Fonction qui affiche les éléments de la liste
    Dans cette version, chaque élément est affiché sur une ligne
    Args:
        li (ListeDoubleChainee): la liste que l'on veut afficher
    """
    courant = li.tete
    print("|", end="")
    while courant:
        print(courant.data, end="|")
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

def ajoutQueueDoublementChainee(li: ListeDoubleChainee, val: int):
    """
    fonction qui ajoute un élément en queue de liste doublement chainée.
    """
    newMaillon = Maillon(data=val)
    if li.queue is None:
        li.tete = newMaillon
        li.queue = newMaillon
    else:
        li.queue.suivant = newMaillon
        newMaillon.precedent = li.queue
        li.queue = newMaillon

def ajoutTete(li: ListeChainee, val: int):
    """
    fonction qui ajoute un élément en tête de liste chainée
    """
    newMaillon = Maillon(data=val, suivant=li.tete)
    li.tete = newMaillon

def ajoutTeteDoublementChainee(li: ListeDoubleChainee, val: int):
    """
    fonction qui ajoute un élément en tête de liste doublement chainée
    """
    newMaillon = Maillon(data=val, suivant=li.tete)
    if li.tete is None:
        li.queue = newMaillon
    else:
        li.tete.precedent = newMaillon
    li.tete = newMaillon

def ajoutEnPos(li: ListeChainee, indice : int, val: int):
    """
    fonction qui ajoute un élément en position donnée de liste chainée
    """
    courant = li.tete
    if indice == 0:
        ajoutTete(li, val)
    else:
        for _ in range(1, indice):
            if courant is None or courant.suivant is None:
                print("Indice trop grand")
                return
            courant = courant.suivant
        if courant is not None:
            if courant is not None:
                newMaillon = Maillon()
                newMaillon.data = val
                newMaillon.suivant = courant.suivant
                courant.suivant = newMaillon

def ajoutEnPosDoublementChainee(li: ListeDoubleChainee, indice : int, val: int):
    """
    fonction qui ajoute un élément en position donnée de liste doublement chainée
    """
    courant = li.tete
    if indice == 0:
        ajoutTeteDoublementChainee(li, val)
    else:
        for _ in range(1, indice):
            if courant is None or courant.suivant is None:
                print("Indice trop grand")
                return
            courant = courant.suivant
        if courant is not None:
            newMaillon = Maillon(data=val)
            newMaillon.suivant = courant.suivant
            courant.suivant = newMaillon
            if newMaillon.suivant is None:
                li.queue = newMaillon
            else:
                newMaillon.suivant.precedent = newMaillon

def suppTete(li : ListeChainee):
    """
    fonction qui supprime un élément en tête de liste chainée
    """
    if li.tete == None:
        print("Liste vide")
    else:
        li.tete = li.tete.suivant

def suppTeteDoublementChainee(li : ListeDoubleChainee):
    """
    fonction qui supprime un élément en tête de liste doublement chainée
    """
    if li.tete == None:
        print("Liste vide")
    else:
        li.tete = li.tete.suivant
        if li.tete == None:
            li.queue = None
        else:
            li.tete.precedent = None


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
        while courant.suivant and courant.suivant.suivant:
            courant = courant.suivant
        if courant.suivant:
            courant.suivant = None

def suppQueueDoublementChainee(li : ListeDoubleChainee):
    """
    fonction qui supprime un élément en queue de liste doublement chainée
    """
    courant = li.tete
    if courant == None:
        print("Liste vide")
    elif courant.suivant == None:
        li.tete = None
        li.queue = None
    else:
        while(courant.suivant.suivant):
            courant = courant.suivant
        courant.suivant = None
        li.queue = courant

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

def suppEnPosDoublementChainee(li: ListeDoubleChainee, indice : int):
    """
    fonction qui supprime un élément en position donnée de liste doublement chainée
    """
    courant = li.tete
    if indice == 0:
        suppTeteDoublementChainee(li)
    else:
        for _ in range(1, indice):
            if courant is None or courant.suivant is None:
                print("Indice trop grand")
                return
            courant = courant.suivant
        if courant is None or courant.suivant is None:
            print("Indice trop grand")
            return
        courant.suivant = courant.suivant.suivant
        if courant.suivant is None:
            li.queue = courant

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

def rechercheDoublementChainee(li: ListeDoubleChainee, val : int) -> int :
    """
    fonction qui recherche un élément dans la liste doublement chainée
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
    print(f"la position est : {recherche(maLC, 2)}")
    print(f"la position est : {recherche(maLC, 4)}")
    print(f"la longueur est : {longueur(maLC)}")

    maLDC = ListeDoubleChainee()
    maLDC.tete = None
    maLDC.queue = None
    afficheListeDoubleChainee(maLDC)
    ajoutTeteDoublementChainee(maLDC, 0)
    afficheListeDoubleChainee(maLDC)
    ajoutTeteDoublementChainee(maLDC, 1)
    afficheListeDoubleChainee(maLDC)
    ajoutTeteDoublementChainee(maLDC, 2)
    afficheListeDoubleChainee(maLDC)
    ajoutQueueDoublementChainee(maLDC, 3)
    afficheListeDoubleChainee(maLDC)
    ajoutQueueDoublementChainee(maLDC, 4)
    afficheListeDoubleChainee(maLDC)
    ajoutEnPosDoublementChainee(maLDC, 2, 5)
    afficheListeDoubleChainee(maLDC)
    ajoutEnPosDoublementChainee(maLDC, 6, 7)
    afficheListeDoubleChainee(maLDC)
    suppTeteDoublementChainee(maLDC)
    afficheListeDoubleChainee(maLDC)
    suppQueueDoublementChainee(maLDC)
    afficheListeDoubleChainee(maLDC)
    suppEnPosDoublementChainee(maLDC, 1)
    afficheListeDoubleChainee(maLDC)
    suppEnPosDoublementChainee(maLDC, 1)
    afficheListeDoubleChainee(maLDC)
    print(f"la position est : {rechercheDoublementChainee(maLDC, 2)}")
    print(f"la position est : {rechercheDoublementChainee(maLDC, 4)}")
    print(f"la longueur est : {longueurDoublementChainee(maLDC)}")
    
    