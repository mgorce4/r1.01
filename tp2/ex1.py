
if __name__ == "__main__" :
    a : float
    b : float
    a = float(input("saisir a: "))
    b = float(input("saisir b: "))
    if(a>b):
        print(a,">",b)
    elif (a<b):
        print(a,"<",b)
    else:
        print(a,"=",b)