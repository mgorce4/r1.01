#impression de triangle isocèles en * selon un nb de lignes entrées

if __name__ == "__main__":
    l:int
    i:int
    j:int

    l=int(input("insérer le nombre de lignes souhaité: "))
    while(l <=0):
        l=int(input("insérer le nombre de lignes souhaité: "))

    for i in range (1,l+1):
        for j in range (1,l-i+1):
            print("  ",end="")
        for j in range (1, 2*i):
            print("* ",end="")
        print()