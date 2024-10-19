

if __name__ == "__main__":
    nombre:int
    nb:int 
    i:int
    j:int
    l:int

    nombre=int(input("entrer nb de rangs: "))
    while (nombre<=0):
        nombre=int(input("entrer nb de rangs: "))


    nb=nombre*2

    for i in range (0,nombre+1):
        for j in range (0,nombre):
            print(nb, end=" ")
            nb=nb-1
        for l in range (0,nombre):
            print(nb,end=" ")
            nb=nb+1
        print(nb)
        print()   
        nb=nb-1
    nb=nb+1
    for i in range (1, nombre+1):
        nb=nb+1
        for j in range (0,nombre):
            print (nb,end=" ")
            nb=nb-1
        for l in range (0,nombre):
            print(nb,end=" ")
            nb=nb+1
        print(nb)
        print()   
        