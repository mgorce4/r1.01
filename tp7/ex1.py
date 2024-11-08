if __name__ == "__main__":
    tab1: list[int]
    tab2: list[int]
    tab3: list[int]
    tab4: list[list[int]]
    avg:int
    i:int
    j:int

    #remplissage d'un tableau
    tab1 = [1, 2, 3, 4, 5,6,7,8,9,10]
    print("tableau 1 : ", tab1)

    #ajout d'un élément
    tab1.append(11)
    print("tableau 1 après ajout : ", tab1)

    #suppression d'un élément
    tab1.remove(5)
    print("tableau 1 après suppression : ", tab1)

    #copie d'un tableau
    tab2 = tab1.copy() 
    print("tableau 2 : ", tab2)

    #concaténation de deux tableaux
    tab3 = tab1 + tab2
    print("tableau 3 : ", tab3)

    #calcul de la moyenne  
    avg = 0
    for i in range(len(tab3)):
        avg += tab3[i]
    avg = avg // len(tab3)
    print("moyenne : ", avg)

    #tableau a deux dimensions
    tab4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("tableau 4 : ", tab4)

    #affichage de la diagonale
    for i in range(len(tab4)):
        print(tab4[i][i])
    
    #affichage de la diagonale inversée
    for i in range(len(tab4)):
        print(tab4[i][len(tab4)-1-i])
    
    #affichage de la matrice
    for i in range(len(tab4)):
        for j in range(len(tab4[i])):
            print(f"| {tab4[i][j]:^3} ", end="")
        print("|")