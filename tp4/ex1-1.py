# suite de fibonacci de 0 à n compris
if __name__ == "__main__":
    un: int
    un1 :int
    un2:int
    n:int

    un=0
    un1=1

    n= int(input("saisir n: "))
    while (n<0):
        n= int(input("saisir n positif: "))
    if (n==0):
        print(un)
    elif (n==1):
        print(un,"\n",un1)
    else:
        print(un,"\n",un1)
        n=n-2
        while (n>=0):
            un2=un+un1
            un=un1
            un1=un2
            n=n-1
            print(un2)
        