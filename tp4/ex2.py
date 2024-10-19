#vérificateur de nombre premier

if __name__ == "__main__":

    nombre:int
    i: int

    nombre = int(input('Écris un nombre entier positif : '))
    while (nombre<=0):
        nombre = int(input('Écris un nombre entier positif : '))
    i = 2

    while (i < nombre and nombre % i != 0 ):
        i = i + 1

    if i == nombre :
        print('Le nombre', nombre, 'est premier ! Fantastique !')

    else :
        print("Ce n'est pas un nombre premier.")