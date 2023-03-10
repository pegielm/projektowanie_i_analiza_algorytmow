import random
def create_tab(n):
    tab = []
    for i in range(1,n):
        tab.append(random.randint(1,100))
    print(tab)
    return tab
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print(arr,end=" ")
        print(key)
        
    print(arr)
                
arr = create_tab(10)
insertion_sort(arr)
