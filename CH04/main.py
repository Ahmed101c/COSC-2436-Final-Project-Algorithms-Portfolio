def quicksort(array):
    """
    Sort an array using the quicksort algorithm.
    
    Args:
        array: List of numbers to sort
        
    Returns:
        Sorted list
    """
  # 1. Base case: if array has fewer than 2 elements, it is already sorted
    if len(array) < 2:
        return array
    
    # 2. Choose the pivot (first element)
    pivot = array[0]
    
    # 3. Partition: elements less than or equal to pivot
    less = [x for x in array[1:] if x <= pivot]
    
    # 4. Partition: elements greater than pivot
    greater = [x for x in array[1:] if x > pivot]
    
    # 5. Combine results recursively
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    # Test cases
    print(quicksort([10, 5, 2, 3]))
    print(quicksort([33, 15, 10]))
    print(quicksort([3, 5, 2, 1, 4]))
    print(quicksort([1]))
    print(quicksort([]))
    print(quicksort([8, 7, 6, 5, 4, 3, 2, 1]))
