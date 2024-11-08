def exPassage(li : list[str], val : int) -> None :
    print("modifications dans la procedure :")
    li[0] = "zero"
    val = val*2
    print(li," valeur = ",val)

def exPassage2(li : list[str], val : int) -> None :
    print("modifications dans la procedure :")
    li[1] = "un"
    val = val*2
    print(li," valeur = ",val)

def décaler_tableau_vers_la_gauche(li : list[int]) -> None :
    last : str
    last=li[0]
    for i in range(len(li)-1):
        li[i] = li[i+1]
    li[len(li)-1] = last

def décaler_tableau_vers_la_droite(li : list[int]) -> None :
    first : str
    first=li[len(li)-1]
    for i in range(len(li)-1,0,-1):
        li[i] = li[i-1]
    li[0] = first

def tri_bulle(tab : list[int]) -> None :
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

def ajouter_element_a_lindice_p(li : list[int], p:int, autre:int) -> None :
    li.append(0)  # Add a dummy element to increase the size of the list
    for i in range(len(li)-1, p, -1):
        li[i] = li[i-1]
    li[p] = autre

def supprimer_element_a_lindice_p(li : list[int], p:int) -> None :
    for i in range(p,len(li)-1):
        li[i] = li[i+1]
    li.pop()

def compter_occurence(li : list[int], p:int) -> int :
    occurence = 0
    for i in range(len(li)):
        if li[i] == p:
            occurence += 1
    return occurence

def intersection(li1 : list[int], li2 : list[int]) -> list[int] :
    li3 = []
    for i in range(len(li1)):
        for j in range(len(li2)):
            if li1[i] == li2[j]:
                li3.append(li1[i])
    return li3

def intersection_sans_doublons(li1 : list[int], li2 : list[int]) -> list[int] :
    li3 = []
    for i in range(len(li1)):
        for j in range(len(li2)):
            if li1[i] == li2[j] and li1[i] not in li3:
                li3.append(li1[i])
    return li3

if __name__ == "__main__":
    maliste : list[str]
    entier  : int
    autre : int
    tab : list[int]
    tab2 : list[int]
    tab3 : list[int]
    p:int
    element:int
    occurence:int
    maliste = ["un", "deux", "trois", "quatre"]
    entier = 10
    tab = [5,6,0,6,9,1,4]
    tab2 = [5,6,0,6,9,1,4,18,72,56,20,63]
    

    print("avant l'appel :")
    print(maliste," entier = ", entier)
    exPassage(maliste, entier)
    print("apres l'appel :")
    print(maliste," entier = ", entier)
    print("deuxième appel :")
    exPassage2(maliste, entier)
    print("apres l'appel :")
    print(maliste," entier = ", entier)
    print("on constate que la liste a été modifiée mais pas l'entier")

    #décalage vers la gauche
    print("décalage vers la gauche")
    print(maliste)
    décaler_tableau_vers_la_gauche(maliste)
    print(maliste)

    #décalage vers la droite
    print("décalage vers la droite")
    print(maliste)
    décaler_tableau_vers_la_droite(maliste)
    print(maliste)

    #ajouter un élément à la fin
    print("ajout d'un élément à la fin")
    print(maliste)
    maliste.append("cinq")
    print(maliste)

    #tri du tableau
    print("tri du tableau")
    print(tab)
    tri_bulle(tab)
    print(tab)

    #ajouter un élément à l'indice p
    p =int(input("saisir l'indice où ajouter l'élément : "))
    element =int(input("saisir l'élément à ajouter : "))
    while p<0 or p>len(tab):
        p =int(input("saisir l'indice où ajouter l'élément : "))
    print(tab)
    ajouter_element_a_lindice_p(tab,p,element)
    print(tab)

    #tri du tableau
    print("tri du tableau")
    print(tab)
    tri_bulle(tab)
    print(tab)

    #suppresion d'un élément a l'indice p
    p =int(input("saisir l'indice où supprimer l'élément : "))
    while p<0 or p>len(tab):
        p =int(input("saisir l'indice où supprimer l'élément : "))
    print(tab)
    supprimer_element_a_lindice_p(tab,p)
    print(tab)

    #compter le nombre d'occurence d'un élément p
    occurence = 0
    p =int(input("saisir l'élément à compter : "))
    occurence = compter_occurence(tab,p)
    print("l'élément ",p," apparait ",occurence," fois dans le tableau")

    #union de deux tableaux
    print("union de deux tableaux")
    print(tab)
    print(tab2)
    tab3 = tab + tab2
    print(tab3)

    #tri du tableau
    print("tri du tableau")
    print(tab3)
    tri_bulle(tab3)
    print(tab3)

    #intersection de deux tableaux
    print("intersection de deux tableaux")
    tab3 = []
    print(tab)
    print(tab2)
    tab3 = intersection(tab,tab2)
    print(tab3)

    #intersection de deux tableaux sans doublons
    print("intersection de deux tableaux sans doublons")
    tab3 = []
    print(tab)
    print(tab2)
    tab3 = intersection_sans_doublons(tab,tab2)
    print(tab3)
