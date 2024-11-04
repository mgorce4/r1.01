menu_options ={
    "1": "nombre de voyelles",
    "2": "palyndrome ?",
    "3": "quitter",
}

def print_menu():
    for key in menu_options.keys():
        print(key, '- -', menu_options[key])

def compte_voyelles(chaine):
    nb_voyelles = 0
    for lettre in chaine:
        if lettre in voyelles:
            nb_voyelles += 1
    return nb_voyelles

def est_palyndrome(mot):
    est_palyndrome = True
    for i in range(len(mot)//2):
        if mot[i] != mot[len(mot)-1-i]:
            est_palyndrome = False
            break
    return est_palyndrome

if __name__ == "__main__":
    chaine :str
    voyelles:set
    n:int
    nb_voyelles:int
    i:int
    mot:str
    palyndrome:bool
    voyelles = {'a', 'e', 'i', 'o', 'u', 'y'}

    while(True):
        print_menu()
        option = ''
        try:
            option = input("choix : ")
        except:
            print("erreur de saisie")
            
        if option == '1':
            chaine = input("saisir une chaine : ")
            nb_voyelles = compte_voyelles(chaine)
            print("nombre de voyelles : ", nb_voyelles)
        elif option == '2':
            mot = input("saisir un mot : ")
            is_palyndrome = est_palyndrome(mot)
            if is_palyndrome:
                print("le mot est un palyndrome")
            else:
                print("le mot n'est pas un palyndrome")
        elif option == '3':
            break
