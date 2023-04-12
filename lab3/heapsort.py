def sortowanie_kopcowe(tablica):
    
    def kopiec(tablica, i, n):
        print(tablica)
        lewy = 2 * i + 1
        prawy = 2 * i + 2
        najwiekszy = i

        if lewy < n and tablica[lewy] > tablica[najwiekszy]:
            najwiekszy = lewy

        if prawy < n and tablica[prawy] > tablica[najwiekszy]:
            najwiekszy = prawy

        if najwiekszy != i:
            tablica[i], tablica[najwiekszy] = tablica[najwiekszy], tablica[i]
            kopiec(tablica, najwiekszy, n)

    n = len(tablica)
    for i in range(n // 2 - 1, -1, -1):
        kopiec(tablica, i, n)

    for i in range(n - 1, 0, -1):
        tablica[i], tablica[0] = tablica[0], tablica[i]
        kopiec(tablica, 0, i)

    return tablica
tablica=[6,3,5,1,4,2,7,8,9,10]
tablica=sortowanie_kopcowe(tablica)
print(tablica)