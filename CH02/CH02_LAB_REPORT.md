## Lab Report

### Student Information
- **Name:** Ahmed Ajlal
- **Date:** 02/02/2026

### Algorithm Analysis

#### Selection Sort
- **Time Complexity:** O(n2)
- **How it works:** 
Selection sort works by repeatedly finding the smallest item in a list and moving it to the correct position. It starts at the beginning of the list, searches through the remaining unsorted items, and selects the smallest value. Then it swaps that value with the current position. This continues until the entire list is sorted.

#### Arrays vs Linked Lists

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      |   O(1)    |    O(n)   | Arrays allow direct access by index, while linked lists must be searched node by node. |
| Insert    |  O(n)     |     O(1)  |Arrays may require shifting elements, while linked lists can insert quickly if the position is already known. |
| Delete    |  0(n)     |     0(1)  | Arrays may require shifting elements after deletion, while linked lists can delete quickly by changing links if the node is known.|

### Reflection Questions

1. Why is selection sort O(n²)?
   Selection sort is O(n²) because it uses nested work to sort the list. For each position in the list, the algorithm searches through the remaining unsorted elements to find the smallest value. As the input size grows, the number of comparisons grows very quickly, which makes selection sort inefficient for large lists.

2. When would you choose a linked list over an array?
  I would choose a linked list over an array when I need to do many insertions or deletions and do not need fast random access by index. Linked lists are useful because they can add or remove nodes by changing links instead of shifting many elements. However, arrays are better when I need to quickly read items using an index.
