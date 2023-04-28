from collections import deque

def bfs(adj_list, start):
    # inicjalizacja kolejki, listy odwiedzonych wierzchołków oraz słownika z odległościami
    queue = deque([start])
    visited = set([start])
    distances = {start: 0}

    # pętla przeszukująca graf
    while queue:
        # pobranie wierzchołka z kolejki
        node = queue.popleft()

        # dodanie nieodwiedzonych sąsiadów do kolejki i odwiedzonych
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                distances[neighbor] = distances[node] + 1

    return distances
# przykładowy graf w postaci listy sąsiedztwa
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

# wywołanie funkcji bfs z wierzchołkiem startowym 0
distances = bfs(graph, 0)

# wyświetlenie odległości od wierzchołka startowego dla każdego wierzchołka w grafie
for vertex, distance in distances.items():
    print(f"Wierzchołek {vertex} ma odległość {distance} od wierzchołka startowego.")
