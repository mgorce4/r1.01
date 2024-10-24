import time

def récursive_puissance_n(n: int, a: int) -> int:
    """
    Fonction permettant de calculer a^n
    entrée : n, a : int
    sortie : res : int
    """
    if n == 0:
        return 1
    else:
        return a * récursive_puissance_n(n - 1, a)

def recurs_a_n(a: int, n: int) -> int:
    """
    Fonction optimisée pour calculer a^n
    entrée : a, n : int
    sortie : res : int
    """
    if a % 2 == 0:
        res = pow(a, n // 2) * pow(a, n // 2)
        return res
    else:
        res = pow(a, (n - 1) // 2) * pow(a, (n - 1) // 2) * a
        return res

if __name__ == "__main__":
    a = int(input("Entrez un entier a : "))
    n = int(input("Entrez un entier n : "))

    while n < 0:
        print("Entrez un entier positif.")
        n = int(input("Entrez un entier n : "))

    # Mesurer le temps pour récursive_puissance_n
    start_time = time.time()
    result1 = récursive_puissance_n(n, a)
    end_time = time.time()
    time_recursive = end_time - start_time

    # Mesurer le temps pour recurs_a_n
    start_time1 = time.time()
    result2 = recurs_a_n(a, n)
    end_time1 = time.time()
    time_recurs_a_n = end_time1 - start_time1

    print(f"La puissance de {a} à la puissance {n} est de {result1}")
    print(f"Temps d'exécution de récursive_puissance_n : {time_recursive:.6f} secondes")

    print(f"La puissance de {a} à la puissance {n} est de {result2}")
    print(f"Temps d'exécution de recurs_a_n : {time_recurs_a_n:.6f} secondes")
