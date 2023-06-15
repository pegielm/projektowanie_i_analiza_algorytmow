def rabin_karp(text, pattern):
    """
    Implementacja algorytmu Rabina-Karpa do wyszukiwania wzorca w tekście.
    
    Args:
        text (str): Tekst, w którym szukamy wzorca.
        pattern (str): Wzorzec do znalezienia.
    
    Returns:
        list: Lista indeksów, na których zaczyna się znaleziony wzorzec.
    """
    indices = []
    n = len(text)
    m = len(pattern)
    prime = 101  # Liczba pierwsza do obliczania sumy kontrolnej
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Obliczanie h = pow(prime, m-1)
    for _ in range(m - 1):
        h = (h * prime) % n
    
    # Obliczanie sumy kontrolnej wzorca i pierwszego okna tekstu
    for i in range(m):
        pattern_hash = (prime * pattern_hash + ord(pattern[i])) % n
        text_hash = (prime * text_hash + ord(text[i])) % n
    
    # Przeszukiwanie tekstu
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Sprawdzenie, czy wzorzec jest rzeczywiście występujący
            j = 0
            while j < m:
                if pattern[j] != text[i + j]:
                    break
                j += 1
            
            if j == m:
                indices.append(i)
        
        # Obliczanie sumy kontrolnej dla następnego okna tekstu
        if i < n - m:
            text_hash = (prime * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % n
            if text_hash < 0:
                text_hash += n
    
    return indices


# Przykład użycia
text = "ABCABCDABCABDA"
pattern = "ABC"
result = rabin_karp(text, pattern)
print("Indeksy znalezionego wzorca:", result)