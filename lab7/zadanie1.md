
```c

LEFT-ROTATE(T, x)
1. y := T[right[x]]   // Przypisz prawe poddrzewo węzła x do zmiennej y.
2. right[x] := left[y]  // Przypisz lewe poddrzewo węzła y do prawego poddrzewa węzła x.
3. if left[y] != nil[T]
4.     p[left[y]] := x  // Jeśli lewe poddrzewo węzła y nie jest nil[T], ustaw jego rodzica na x.
5. p[y] := p[x]        // Przypisz rodzica węzła x do zmiennej p[y].
6. if p[x] = nil[T]
7.     root[T] := y    // Jeśli x jest korzeniem drzewa, przypisz y jako nowy korzeń.
8. else if x = left[p[x]]
9.     left[p[x]] := y // Jeśli x jest lewym dzieckiem swojego rodzica, przypisz y jako nowe lewe dziecko.
10.else
11.    right[p[x]] := y // W przeciwnym razie przypisz y jako nowe prawe dziecko.
12. left[y] := x       // Przypisz x jako lewe poddrzewo y.
13. p[x] := y          // Przypisz y jako rodzica x.

```