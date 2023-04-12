def szybkie_sortowanie(tablica):
    print(tablica)
    if len(tablica) <= 1:
        return tablica
    
    pivot = tablica.pop(0)
    mniejsze = []
    wieksze = []
    
    for element in tablica:
        if element < pivot:
            mniejsze.append(element)
        else:
            wieksze.append(element)
    
    return szybkie_sortowanie(mniejsze) + [pivot] + szybkie_sortowanie(wieksze)
tablica=[4,6,3,5,1,2]
tablica=szybkie_sortowanie(tablica)
print(tablica)