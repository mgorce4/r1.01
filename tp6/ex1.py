def ecart (j1:int,j2:int,m1:int,m2:int,an1:int,an2:int):
    """
    fonction permettant de calculer l'écart d'âge entre deux dates
    entrée : j1,m1,an1,j2,m2,an2 : int
    sortie : age : int
    """

    age:int
    exchange_day:int
    exchange_month:int
    exchange_year:int
    if (an2<an1) or (an1==an2 and m2<m1) or (an1==an2 and m1==m2 and j2<j1):
        exchange_day=j1
        j1=j2
        j2=exchange_day
        exchange_month=m1
        m1=m2
        m2=exchange_month
        exchange_year=an1
        an1=an2
        an2=exchange_year

    age = an2 - an1
    if((m2 < m1) or ((m2 == m1) and (j2 < j1))):
        age = age - 1

    return age

def vérifier_date(jour:int,mois:int,annee:int):
    est_biss:bool
    mois_ok:bool
    jour_ok:bool
    fevrier_ok:bool
    date_ok :bool

    est_biss=((annee%4==0)and(annee%100!=0)) or (annee%400==0)
    mois_ok=((mois>=1) and (mois <=12))
    fevrier_ok=((est_biss)and (jour<=29)) or (est_biss==False) and (jour<=28)
    jour_ok= ((jour>=1) and (fevrier_ok or ((mois!=2 and mois != 4 and mois!=6 and mois!=9 and mois !=11) and jour<=31) or ((mois==4 or mois==6 or mois==9 or mois==11)and jour <=30)) )
    date_ok= jour_ok and mois_ok and (annee>1582)

    return date_ok

if __name__ == "__main__":
    print("Entrez la date de naissance de la première personne :")
    j1 = int(input("Jour : "))
    m1 = int(input("Mois : "))
    an1 = int(input("Année : "))
    while not vérifier_date(j1,m1,an1):
        print("Date incorrecte.")
        print("Entrez la date de naissance de la première personne :")
        j1 = int(input("Jour : "))
        m1 = int(input("Mois : "))
        an1 = int(input("Année : "))
    print("Entrez la date ou vous voulez connaître l'écart avec la première :")
    j2 = int(input("Jour : "))
    m2 = int(input("Mois : "))
    an2 = int(input("Année : "))
    while not vérifier_date(j2,m2,an2):
        print("Date incorrecte.")
        print("Entrez la date ou vous voulez connaître l'écart avec la première :")
        j2 = int(input("Jour : "))
        m2 = int(input("Mois : "))
        an2 = int(input("Année : "))
    print("L'écart d'âge entre les deux dates est de", ecart(j1,j2,m1,m2,an1,an2), "ans.")

