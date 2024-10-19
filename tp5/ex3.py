if __name__ == "__main__":
    rows: int

    rows=int(input("entrer nb de rangs: "))
    while (rows<=0):
        rows=int(input("entrer nb de rangs: "))


    for i in range (0, rows):
        for j in range (0,i+1):
            print(j+1, end="")
        print()