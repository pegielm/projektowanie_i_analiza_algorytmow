def sortowanie_scalanie(tablica):
    def scalanie(tablica_lewa, tablica_prawa):
        i = j = 0
        scalona_tablica = []
        
        while i < len(tablica_lewa) and j < len(tablica_prawa):
            if tablica_lewa[i] <= tablica_prawa[j]:
                scalona_tablica.append(tablica_lewa[i])
                i += 1
            else:
                scalona_tablica.append(tablica_prawa[j])
                j += 1
        
        if i < len(tablica_lewa):
            scalona_tablica.extend(tablica_lewa[i:])
        
        if j < len(tablica_prawa):
            scalona_tablica.extend(tablica_prawa[j:])
        
        return scalona_tablica

    if len(tablica) <= 1:
        return tablica
    
    srodek = len(tablica) // 2
    tablica_lewa = sortowanie_scalanie(tablica[:srodek])
    tablica_prawa = sortowanie_scalanie(tablica[srodek:])
    
    return scalanie(tablica_lewa, tablica_prawa)
tablica=[6,3,5,1,4,2]
tablica=sortowanie_scalanie(tablica)
print(tablica)