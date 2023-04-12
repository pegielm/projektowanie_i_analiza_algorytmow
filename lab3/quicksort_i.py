def szybkie_sortowanie(tablica, lewy, prawy):
    if lewy < prawy:
        # Wybierz pivot jako ostatni element
        pivot = tablica[prawy]
        # Podział na elementy mniejsze i większe od pivot
        i = lewy - 1
        for j in range(lewy, prawy):
            if tablica[j] <= pivot:
                i += 1
                tablica[i], tablica[j] = tablica[j], tablica[i]
        # Umieść pivot w odpowiedniej pozycji
        tablica[i+1], tablica[prawy] = tablica[prawy], tablica[i+1]
        # Rekurencyjnie posortuj elementy mniejsze i większe od pivot
        szybkie_sortowanie(tablica, lewy, i)
        szybkie_sortowanie(tablica, i+2, prawy)
    return tablica
tablica=[4,6,3,5,1,2]
tablica=szybkie_sortowanie(tablica, 0, len(tablica)-1)
print(tablica)