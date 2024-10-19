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
    day:int
    month:int
    year:int

    day=int(input("entrer un jour: "))
    month=int(input("entrer un mois: "))
    year=int(input("entrer une annee: "))

    if vérifier_date(day,month,year):
        print("la date est juste")
    else:
        print("la date est fausse")