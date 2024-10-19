def nb_parfait(nombre):
    somme = 0  # Initialiser la somme des diviseurs

    # Boucle de 1 à nombre//2 pour vérifier les diviseurs
    for compteur_i in range(1, nombre // 2 + 1):
        if nombre % compteur_i == 0:  # Vérifie si compteur_i est un diviseur
            somme += compteur_i  # Ajoute le diviseur à la somme

    return somme == nombre  # Retourne True si la somme des diviseurs est égale au nombre


if __name__ == "__main__":
    nombre = int(input("Entrez un nombre pour vérifier s'il est parfait: "))

    while nombre <= 0:
        nombre = int(input("Veuillez entrer un nombre positif: "))

    if nb_parfait(nombre):
        print(nombre, "est un nombre parfait")
    else:
        print(nombre, "n'est pas un nombre parfait")
