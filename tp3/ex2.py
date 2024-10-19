if __name__ == "__main__":
    a: int
    b: int
    c: int

    print("Trouveur de PGCD:")
    a = int(input("saisir a: "))
    while (a<=0):
        a = int(input("saisir a superieur et different de 0: "))
    b = int(input("saisir b: "))
    while (b<=0):
        b = int(input("saisir b superieur et different de 0: "))

    while (a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    print("le PGCD est ", a)