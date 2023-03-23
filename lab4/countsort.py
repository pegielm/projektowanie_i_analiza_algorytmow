import random
def sortowanie_przez_zliczanie(tablica : list):
    n = len(tablica)
    najwiekszy = max(tablica) #moze byc ustalona znana najwieksz wartosc
    wynik =[0 for i in tablica]
    print(wynik)
    zliczanie=[0 for i in range(najwiekszy+1)]
    for element in tablica:
        zliczanie[int(element)]+=1
    #zliczanie[i] to element w koncowej tablice gdzie ma byc i
    print(zliczanie)
    for i in range(1,najwiekszy+1):
        zliczanie[i]+=zliczanie[i-1]
    print(zliczanie)
    #po kolei kazdy elemement z poczatkowej tablicy jest kładziony na swoją pozycje 
    for i in range(n):
        wynik[zliczanie[tablica[i]]-1]=tablica[i]
        zliczanie[tablica[i]]-=1
    return wynik

    
tablica = [random.randint(1,100) for i in range(100)]
tablica=sortowanie_przez_zliczanie(tablica)
print(tablica)