"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # =========================================
    # Load city data
    # =========================================
    cities = load_cities('data/cities.json')          # Load cities from the JSON file
    print(f"Loaded {len(cities)} cities\n")           # Print how many records were loaded

    # =========================================
    # PART 1: Selection Sort
    # =========================================
    print("=========================================")
    print("PART 1: Selection Sort")
    print("=========================================")

    # ---- Selection sort (ascending by population) ----
    start = time.time()                               # Start timing selection sort
    sorted_asc = selection_sort(cities, key=lambda c: c["population"])
    end = time.time()                                 # End timing
    print(f"\nSelection sort (ascending) took {end - start:.6f} seconds")

    print("\nTop 5 smallest cities (by population):")
    for city in sorted_asc[:5]:                        # First 5 are smallest after ascending sort
        print(f"{city['city']} - {city['population']}")

    # ---- Selection sort (descending by population) ----
    start = time.time()
    sorted_desc = selection_sort(cities, key=lambda c: c["population"], reverse=True)
    end = time.time()
    print(f"\nSelection sort (descending) took {end - start:.6f} seconds")

    print("\nTop 5 largest cities (by population):")
    for city in sorted_desc[:5]:                       # First 5 are largest after descending sort
        print(f"{city['city']} - {city['population']}")

    # ---- Compare with Python built-in sort (Timsort) ----
    start = time.time()
    builtin_sorted = python_builtin_sort(cities, key=lambda c: c["population"])
    end = time.time()
    print(f"\nPython built-in sort took {end - start:.6f} seconds")

    # =========================================
    # PART 2: Array vs Linked List
    # =========================================
    print("\n=========================================")
    print("PART 2: Array vs Linked List")
    print("=========================================")

    # ---- Array (Python list) demonstration ----
    print("\nArray (Python list) operations:")

    # Access by index is O(1) because Python can jump directly to that memory location
    print(f"Access by index [0] (O(1)): {cities[0]['city']}")

    # Insert at beginning is O(n) because all existing items must shift right by 1
    start = time.time()
    cities.insert(0, {"city": "Test City", "population": 0})
    end = time.time()
    print(f"Insert at beginning (O(n)) took {end - start:.6f} seconds")

    # ---- Linked List demonstration ----
    print("\nLinked List operations:")
    ll = LinkedList()                                  # Create an empty linked list

    # Insert cities into linked list (depends on implementation, but generally O(1) per head insert)
    for city in cities:
        ll.insert(city)

    # Insert at head is O(1) because we only change pointers (no shifting)
    start = time.time()
    ll.insert({"city": "Test City", "population": 0})
    end = time.time()
    print(f"Insert at head (O(1)) took {end - start:.6f} seconds")

    # Searching is O(n) because we may need to check nodes one by one
    search_name = cities[len(cities) // 2]["city"]     # Pick a city name to search for
    start = time.time()
    found = ll.search(search_name)
    end = time.time()
    print(f"Search for '{search_name}' (O(n)) took {end - start:.6f} seconds")
    print(f"Found? {found}")

    # =========================================
    # PART 3: Big O Comparison
    # =========================================
    print("\n=========================================")
    print("PART 3: Big O Summary")
    print("=========================================")

    print("\nSorting Algorithms:")
    print("  Selection Sort:      O(n^2)")
    print("  Python Timsort:      O(n log n)")

    print("\nArray vs Linked List:")
    print("  Operation                 Array (List)       Linked List")
    print("  --------------------------------------------------------")
    print("  Access by index            O(1)              O(n)")
    print("  Insert at beginning        O(n)              O(1)")
    print("  Search by value            O(n)              O(n)")


if __name__ == "__main__":
    main()
