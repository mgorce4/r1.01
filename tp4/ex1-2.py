#suite de fibonacci de 0 à n exclu
if __name__ == "__main__":
    un: int
    un1 :int
    un2:int
    borne_sup:int

    un=0
    un1=1

    borne_sup= int(input("saisir la borne supérieure: "))
    while (borne_sup<0):
        borne_sup= int(input("saisir une borne supérieure positive: "))
    if (borne_sup==0):
        print(un)
    elif (borne_sup==1):
        print(un,"\n",un1)
    else:
        print(un,"\n",un1)
        borne_sup=borne_sup-2
        while (borne_sup>0):
            un2=un+un1
            un=un1
            un1=un2
            borne_sup=borne_sup-1
            print(un2)