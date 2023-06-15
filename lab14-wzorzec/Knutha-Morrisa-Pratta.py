def compute_prefix_table(pattern):
    """
    Funkcja pomocnicza do obliczania tablicy prefiksowej dla algorytmu KMP.
    
    Args:
        pattern (str): Wzorzec, dla którego obliczana jest tablica prefiksowa.
    
    Returns:
        list: Tablica prefiksowa.
    """
    m = len(pattern)
    prefix_table = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i += 1
    print(f"prefix_table = {prefix_table}")
    return prefix_table


def kmp(text, pattern):
    """
    Implementacja algorytmu Knutha-Morrisa-Pratta (KMP) do wyszukiwania wzorca w tekście.
    
    Args:
        text (str): Tekst, w którym szukamy wzorca.
        pattern (str): Wzorzec do znalezienia.
    
    Returns:
        list: Lista indeksów, na których zaczyna się znaleziony wzorzec.
    """
    indices = []
    n = len(text)
    m = len(pattern)
    prefix_table = compute_prefix_table(pattern)
    i = j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == m:
                indices.append(i - j)
                j = prefix_table[j - 1]
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1
    
    return indices


# Przykład użycia
text = "ABCAABCADABCABDA"
pattern = "AABCA"
result = kmp(text, pattern)
print("Indeksy znalezionego wzorca:", result)
