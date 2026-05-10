from typing import List, Any

class HashTable:
    def __init__(self, size: int):
        """Initialize the hash table with given size."""
        self.size = size
        self.table: List[Any] = [None] * size  # 

    def hash_function(self, key: Any) -> int:
        """Compute the hash value for a given key."""
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)

        # Linear probing
        start_index = index
        while self.table[index] is not None:
            
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)

    def search(self, key: Any) -> Any:
        """Search for the value associated with a key in the hash table."""
        index = self.hash_function(key)
        start_index = index

        # Linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break

        return None


if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert("apple", 100)
    hash_table.insert("banana", 200)
    hash_table.insert("orange", 300)

    print(hash_table.search("apple"))   # 100
    print(hash_table.search("banana"))  # 200
    print(hash_table.search("orange"))  # 300
    print(hash_table.search("grape"))   # None
