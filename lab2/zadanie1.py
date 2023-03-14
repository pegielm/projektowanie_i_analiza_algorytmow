import random
def merge(tablica_lewa, tablica_prawa):
    tablica_koncowa=[]
    l = 0
    p = 0
    while l<len(tablica_lewa) and p <len(tablica_prawa):
        if tablica_lewa[l]<tablica_prawa[p]:
            tablica_koncowa.append(tablica_lewa[l])
            l=l+1
        else:
            tablica_koncowa.append(tablica_prawa[p])
            p=p+1
    while l < len(tablica_lewa):
        tablica_koncowa.append(tablica_lewa[l])
        l=l+1
    while p < len(tablica_prawa):
        tablica_koncowa.append(tablica_prawa[p])
        p=p+1
    #print(tablica_koncowa)



def mergesort(tablica):
    #print("mergesort dla "+str(tablica))
    if len(tablica) > 1:
        
        srodek = (len(tablica))// 2
        tablica_lewa = mergesort(tablica[:srodek])
        tablica_prawa = mergesort(tablica[srodek:])
        tablica_koncowa=[]
        l = 0
        p = 0
        while l<len(tablica_lewa) and p<len(tablica_prawa):
            if tablica_lewa[l]<tablica_prawa[p]:
                tablica_koncowa.append(tablica_lewa[l])
                l=l+1
            else:
                tablica_koncowa.append(tablica_prawa[p])
                p=p+1
        while l < len(tablica_lewa):
            tablica_koncowa.append(tablica_lewa[l])
            l=l+1
        while p < len(tablica_prawa):
            tablica_koncowa.append(tablica_prawa[p])
            p=p+1
        #print("tablica koncowa" + str(tablica_koncowa))
        return tablica_koncowa[:]
    else:
        return tablica[:]

            
tablica = []
n = 200
while n>0:
    tablica.append(random.randint(1,n))
    n=n-1
tablica = mergesort(tablica)
print(tablica)

