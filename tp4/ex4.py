#vérificateur de date et date du jour suivant

if __name__ == "__main__":
    day: int
    month: int
    year: int
    day=(int(input("saisir le jour: ")))
    month=(int(input("saisir le mois: ")))
    year=(int(input("saisir l'année': ")))

    if month in[1,3,5,7,8,10,12]:
        while(day<=0 or day>31):
            print("la date est incorrecte")
            day=(int(input("saisir un jour correcte: ")))
        if month in[1,3,5,7,8,10]:
            if(day==31):
                print("01/",month+1,"/",year)
            else:
                print(day+1,"/",month,"/",year)
        else:
            if(day==31):
                print("01/01/",year+1)
            else:
                print(day+1,"/",month,"/",year)

    elif month in [4,6,9,11]:
        while (day<=0 or day>30):
            print("la date est incorrecte")
            day=(int(input("saisir un jour correcte: ")))
        if(day==30):
                print("01/",month+1,"/",year)
        else:
            print(day+1,"/",month,"/",year)

    elif (month==2):
        if(year%400==0):
            while(day<=0 or day>29):
                day=(int(input("saisir un jour correcte: ")))
            if(day==29):
                print("01/",month+1,"/",year)
            else:
                print(day+1,"/",month,"/",year)
        else:
            while(day<=0 or day>28):
                day=(int(input("saisir un jour correcte: ")))
            if(day==28):
                print("01/",month+1,"/",year)
            else:
                print(day+1,"/",month,"/",year)
    else:
        print("la date est incorrecte") 
        