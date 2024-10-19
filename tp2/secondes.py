
if __name__ == "__main__" :
    second : int
    minute :int
    hour : int
    day : int
    week : int
    month : int
    year: int
    time: int


    print("---bienvenue--\nChoisissez depuis quelle unité temporelle vous voulez traduire dans les autres:")
    print("1-secondes\n2-minutes\n3-heures\n4-jours\n5-semaines\n6-mois\n7-annees\n")
    time= int(input("votre choix: "))
    while(time<1 or time>7):
        print("---bienvenue--\nChoisissez depuis quelle unite temporelle vous voulez traduire dans les autres:")
        print("1-secondes\n2-minutes\n3-heures\n4-jours\n5-semaines\n6-mois\n7-années\n")
        time= int(input("choisissez parmis la liste: "))

    if (time ==1):
        second = int(input("saisir le nombre de secondes: "))
        while (second<0):
            second = int(input("saisir le nombre de secondes superieur à 0: "))
        minute = second//60 
        hour = minute//60
        day = hour//24 
        week = day//7
        month = day//30
        year = day//364 
        if (second<3600):
            print("secondes: ",second," nb de minutes: ",minute)
        elif(second<86400):
            print("secondes: ",second," nb de minutes: ",minute," nb d'heures: ",hour)
        elif(day<7):
            print("secondes: ",second," nb de minutes: ",minute," nb d'heures: ",hour," nb de jours: ",day)
        elif(day<30):
            print("secondes: ",second," nb de minutes: ",minute," nb d'heures: ",hour," nb de jours: ",day," nb de semaine: ",week)
        elif(day<364):
            print("secondes: ",second," nb de minutes: ",minute," nb d'heures: ",hour," nb de jours: ",day," nb de semaine: ",week, " nb de mois: ", month)
        else:
            print("secondes: ",second," nb de minutes: ",minute," nb d'heures: ",hour," nb de jours: ",day," nb de semaine: ",week, " nb de mois: ", month," nb d'annees: ",year)
    elif(time==2):
        minute = int(input("saisir le nombre de minutes: "))
        while (minute<0):
            minute = int(input("saisir le nombre de minutes superieur a 0: "))
        second=(minute*60 )
        hour=(minute//60 )
        day=(minute//1440)
        week=(minute//10080)
        month=minute//43800
        year = minute//525600
        print("nb de secondes: ",second,"nb de minutes: ",minute,"nb d'heures: ",hour,"nb de jours: ",day,"nb de mois: ",month,"nb d'annees: ",year)
    elif(time==3):
        hour = int(input("saisir le nombre d'heures': "))
        while (hour<0):
            hour = int(input("saisir le nombre d'heures superieur a 0: "))
        second=hour*3600
        minute=hour*60
        day=hour//24
        week=hour//1440
        month=day//30
        year=minute//525600
        print("nb de secondes: ",second,"nb de minutes: ",minute,"nb d'heures: ",hour,"nb de jours: ",day,"nb de mois: ",month,"nb d'annees: ",year)
    elif time==4:
        day = int(input("saisir le nombre de jours': "))
        while (day<0):
            day = int(input("saisir le nombre de jours superieur a 0: "))
        hour= day*24
        minute=hour*60
        second=minute*60
        week= day//7
        month=day//30
        year=minute//525600
        print("nb de secondes: ",second,"nb de minutes: ",minute,"nb d'heures: ",hour,"nb de jours: ",day,"nb de mois: ",month,"nb d'annees: ",year)
    elif time==5:
        week = int(input("saisir le nombre de semaines': "))
        while (week<0):
            week = int(input("saisir le nombre de semaines superieur a 0: "))
        day=week*7
        hour=day*24
        minute=hour*60
        second=minute*60
        month=day//30
        year=minute//525600
        print("nb de secondes: ",second,"nb de minutes: ",minute,"nb d'heures: ",hour,"nb de jours: ",day,"nb de mois: ",month,"nb d'annees: ",year)
    elif time==6:
        month = int(input("saisir le nombre de mois': "))
        while (month<0):
            month = int(input("saisir le nombre de mois superieur a 0: "))
        week=month*30
        day=week*7
        hour=day*24
        minute=hour*60
        second=minute*60
        year=minute//525600
        print("nb de secondes: ",second,"nb de minutes: ",minute,"nb d'heures: ",hour,"nb de jours: ",day,"nb de mois: ",month,"nb d'annees: ",year)
    else:
        year = int(input("saisir le nombre d'annees': "))
        while (year<0):
            year = int(input("saisir le nombre d'annees superieur a 0: "))
        month=year*12
        week=year*52
        day=year*365
        hour=day*24
        minute=hour*60
        second=minute*60
        print("nb de secondes: ",second,"nb de minutes: ",minute,"nb d'heures: ",hour,"nb de jours: ",day,"nb de mois: ",month,"nb d'annees: ",year)
