def sortowanie_przez_wstawianie(lista):
    n = len(lista)
    for i in range(1, n):
        print(lista)
        klucz = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > klucz:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = klucz
    return lista
tablica=[6,3,5,1,4,2,7,8,9,10]
tablica=sortowanie_przez_wstawianie(tablica)
print(tablica)
