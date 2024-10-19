import math

if __name__ == "__main__" :
    a : float
    b : float
    c: float
    d :float
    x1: float
    x2:float

    a = float(input("saisir a: "))
    b= float(input("saisir b: "))
    c = float(input("saisir c: "))

    if (a==0):
        if b!=0:
            x1 = -c/b
            print ("la seule racine existante est ", x1)
        else:
            if c!=0:
                print("L'equation est la racine")
            else:
                print("la racine est n'importe quel reel")

    else:
        d = (b*b-4.0*a*c)
        if d==0:
            x1 = -b/(2.0*a)
            print("la racine reele est ", x1)
        elif d>0 :
            x1 = (-b - math.sqrt(d)/2*a)
            x2 = (-b + math.sqrt(d)/2*a)
            print("les racines réelles sont ",x1, " et ",x2)
        else:
            print("il n'y a pas de racines réelles")