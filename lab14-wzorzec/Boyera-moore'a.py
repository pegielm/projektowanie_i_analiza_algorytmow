def generate_bad_char_table(pattern):
    """
    Generuje tablicę zła znakowego przesunięcia dla algorytmu Boyera-Moore'a.
    
    Args:
        pattern (str): Wzorzec, dla którego generowana jest tablica.
    
    Returns:
        dict: Tablica zła znakowego przesunięcia.
    """
    table = {}
    m = len(pattern)
    
    for i in range(m - 1):
        table[pattern[i]] = m - i - 1
    
    return table


def generate_good_suffix_table(pattern):
    """
    Generuje tablicę dobrej sufiksowej przesunięcia dla algorytmu Boyera-Moore'a.
    
    Args:
        pattern (str): Wzorzec, dla którego generowana jest tablica.
    
    Returns:
        list: Tablica dobrej sufiksowej przesunięcia.
    """
    m = len(pattern)
    suffixes = [0] * m
    border = 0
    
    for i in range(m - 1, -1, -1):
        if is_suffix(pattern, i + 1):
            border = i + 1
        suffixes[i] = border
    
    for i in range(m - 1):
        length = get_suffix_length(pattern, i)
        if pattern[i - length] != pattern[m - 1 - length]:
            suffixes[m - 1 - length] = m - 1 - i + length
    
    return suffixes


def is_suffix(pattern, p):
    """
    Sprawdza, czy dany indeks p jest końcem sufiksu w danym wzorcu.
    
    Args:
        pattern (str): Wzorzec.
        p (int): Indeks do sprawdzenia.
    
    Returns:
        bool: True, jeśli indeks jest końcem sufiksu; False w przeciwnym razie.
    """
    m = len(pattern)
    i = 0
    j = p
    
    while j < m:
        if pattern[i] != pattern[j]:
            return False
        i += 1
        j += 1
    
    return True


def get_suffix_length(pattern, p):
    """
    Oblicza długość sufiksu w danym wzorcu, zaczynając od indeksu p.
    
    Args:
        pattern (str): Wzorzec.
        p (int): Indeks początkowy sufiksu.
    
    Returns:
        int: Długość sufiksu.
    """
    length = 0
    i = p
    j = len(pattern) - 1
    
    while i >= 0 and pattern[i] == pattern[j]:
        length += 1
        i -= 1
        j -= 1
    
    return length


def boyer_moore(text, pattern):
    """
    Implementacja algorytmu Boyera-Moore'a do wyszukiwania wzorca w tekście.
    
    Args:
        text (str): Tekst, w którym szukamy wzorca.
        pattern (str): Wzorzec do znalezienia.
    
    Returns:
        list: Lista indeksów, na których zaczyna się znaleziony wzorzec.
    """
    indices = []
    n = len(text)
    m = len(pattern)
    bad_char_table = generate_bad_char_table(pattern)
    good_suffix_table = generate_good_suffix_table(pattern)
    i = 0
    
    while i <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0:
            indices.append(i)
            i += good_suffix_table[0]
        else:
            bad_char_shift = bad_char_table.get(text[i + j])
            good_suffix_shift = good_suffix_table[j]
            i += max(bad_char_shift, good_suffix_shift)
    
    return indices


# Przykład użycia
text = "ABCABCDABCABDA"
pattern = "ABC"
result = boyer_moore(text, pattern)
print("Indeksy znalezionego wzorca:", result)
