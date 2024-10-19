

if __name__ == "__main__":
    a: int
    b: int
    resultat: int
    choix: int
    operateur: int

    print("bienvenue\nVeuillez choisir un opérateur:")
    print("1-addition\n2-soustraction\n3-multiplication\n4-division")

    operateur= int(input("votre choix: "))
    while (operateur<1 or operateur>4):
        print("bienvenue\nVeuillez choisir un opérateur:")
        print("1-addition\n2-soustraction\n3-multiplication\n4-division")

        operateur= int(input("votre choix: "))
    a = int(input("saisir a: "))
    b = int(input("saisir b: "))

    if (operateur==1):
        resultat=a+b
        print(a,"+",b,"=",resultat)
    elif (operateur==2):
        resultat=a-b
        print(a,"-",b,"=",resultat)
    elif (operateur==3):
        resultat=a*b
        print(a,"*",b,"=",resultat)
    else:
        if (b==0):
            print("la division par 0 est impossible souhaitez vous changer de valeur?")
            print("1-oui\n2-non")
            choix= int(input("votre choix: "))
            while (choix<1 or choix>2):
                print("la division par 0 est impossible souhaitez vous changer de valeur?")
                print("1-oui\n2-non")
                choix= int(input("votre choix: "))
            if (choix==1):
                b = int(input("saisir b: "))
                while(b==0):
                    b = int(input("saisir b: "))
                    resultat =a//b
                    print(a,"/",b,"=",resultat)
            else:
                print("au revoir")
        else:
            resultat =a//b
            print(a,"/",b,"=",resultat)