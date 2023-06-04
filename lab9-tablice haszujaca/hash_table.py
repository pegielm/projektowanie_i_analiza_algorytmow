class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Funkcja haszująca - przykładowa implementacja
        return len(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found in the hash table.")
    def print(self):
        print(self.table)
hash_table = HashTable(10)

# Wstawianie elementów
hash_table.insert("klucz1", "wartosc1")
hash_table.insert("klucz2", "wartosc2")
hash_table.insert("klucz3", "wartosc3")
hash_table.insert("klucz4", "wartosc4")


# Pobieranie wartości
print(hash_table.get("klucz1"))  # Output: wartosc1
print(hash_table.get("klucz3"))  # Output: wartosc3

# Aktualizowanie wartości
hash_table.insert("klucz1", "nowa_wartosc1")
print(hash_table.get("klucz1"))  # Output: nowa_wartosc1

# Usuwanie elementów
hash_table.remove("klucz2")
print(hash_table.get("klucz2"))  # Output: None

hash_table.print()
# Próba usunięcia nieistniejącego elementu
hash_table.remove("klucz5")  # Raises KeyError: Key 'klucz5' not found in the hash table.
