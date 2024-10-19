if __name__ == "__main__":
    day: int
    month: int
    year: int
    day=(int(input("saisir le jour: ")))
    month=(int(input("saisir le mois: ")))
    year=(int(input("saisir l'année': ")))

    if month in[1,3,5,7,8,10,12]:
        if(day<=0 or day>31):
            print("la date est incorrecte")
        else:
            print("la date est correcte")
    elif month in [4,6,9,11]:
        if (day<=0 or day>30):
            print("la date est incorrecte")
        else:
            print("la date est correcte")
    elif (month==2):
        if(year%400==0):
            if(day<=0 or day>29):
                print("la date est incorrecte")
            else:
                print("la date est correcte")
        else:
            if(day<=0 or day>28):
                print("la date est incorrecte")
            else:
                print("la date est correcte")
    else:
        print("la date est incorrecte")