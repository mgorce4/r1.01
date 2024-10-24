def sommeR(n:int):
    """
    fonction permettant de calculer la somme des n premiers entiers
    entrée : n : int
    sortie : somme : int
    """
    if (n==1):
        return 1
    else:
        return n + sommeR(n-1)
    
if __name__ == "__main__":
    n = int(input("Entrez un entier n : "))
    while n < 0:
        print("Entrez un entier positif.")
        n = int(input("Entrez un entier n : "))
    print("La somme des",n,"premiers entiers est de",sommeR(n))