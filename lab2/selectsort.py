def sortowanie_przez_wybieranie(lista):
    n = len(lista)
    for i in range(n):
        indeks_minimalnego = i
        for j in range(i+1, n):
            if lista[j] < lista[indeks_minimalnego]:
                indeks_minimalnego = j
        lista[i], lista[indeks_minimalnego] = lista[indeks_minimalnego], lista[i]
    return lista
tablica=[6,3,5,1,4,2,7,8,9,10]
tablica=sortowanie_przez_wybieranie(tablica)
print(tablica)
