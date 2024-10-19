if __name__ == "__main__" :
    hauteurPiece : int
    largeurPiece : int
    hauteurCarreau : int
    largeurCarreau : int
    joint : int
    nbl : int
    nbh :int
    resultat : int
    hauteurPiece = int(input("saisir la hauteur de la piece:"))
    largeurPiece =int(input("saisir la largeur de la piece: "))
    hauteurCarreau = int(input("saisir la hauteur d'un carreau: "))
    largeurCarreau = int(input("saisir la largeur d'un carreau: "))
    joint = int(input("saisir la largeur des joints: "))
    while (largeurCarreau <=0 or hauteurCarreau <=0 or largeurPiece<=0 or hauteurPiece<=0 or joint<=0 or largeurPiece<=largeurCarreau+2*joint or hauteurPiece<=hauteurCarreau+2*joint ):
        print("des erreurs sont presentent dans les valeurs entrees")
        hauteurPiece = int(input("saisir la hauteur de la piece:"))
        largeurPiece =int(input("saisir la hlargeur de la piece: "))
        hauteurCarreau = int(input("saisir la hauteur d'un carreau: "))
        largeurCarreau = int(input("saisir la largeur d'un carreau: "))
        joint = int(input("saisir la largeur des joints: "))
    nbl=((largeurPiece-joint)//(largeurCarreau+joint))+1
    nbh=((hauteurPiece-joint)//(hauteurCarreau+joint))+1
    resultat =nbl*nbh
    print("il faut ",resultat," carreaux")