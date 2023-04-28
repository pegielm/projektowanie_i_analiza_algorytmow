from collections import deque

def bfs(V, E, s):
    # inicjalizacja odległości wierzchołków od źródła
    d = {u: float('inf') for u in V}
    d[s] = 0
    
    # inicjalizacja kolejki
    Q = deque()
    Q.append(s)
    
    # pętla przeszukująca graf
    while Q:
        # pobranie wierzchołka z kolejki
        u = Q.popleft()

        # przeglądanie sąsiadów wierzchołka u
        for v in E[u]:
            if d[v] == float('inf'):
                d[v] = d[u] + 1
                Q.append(v)

    return d
