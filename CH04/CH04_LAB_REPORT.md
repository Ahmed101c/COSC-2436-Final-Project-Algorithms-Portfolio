Lab 04: Quicksort

Student Information

Name: Ahmed Ajlal
Date: 2/21/2026
Quicksort Concepts

Divide and Conquer

Quicksort divides the array into smaller parts around a pivot, recursively sorts those parts, and combines them to form the final sorted array.

The Three Steps

Choose pivot: Select one element (e.g., first element) to act as the reference point.

Partition: Split the array into two groups: elements ≤ pivot and elements > pivot.

Recurse and combine: Recursively sort both groups, then combine: sorted_less + [pivot] + sorted_greater

Tracing Quicksort

Trace: quicksort([3, 5, 2, 1, 4])

Trace: quicksort([3, 5, 2, 1, 4]) Pivot = 3 Less = [2, 1] Greater = [5, 4] quicksort([2, 1]) Pivot = 2 Less = [1] Greater = [] → [1, 2] quicksort([5, 4]) Pivot = 5 Less = [4] Greater = [] → [4, 5] Final result: [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]

Complexity Analysis

Case	Time Complexity	Why?
Best	O(n log n)	Pivot splits array evenly each time.
Average	O(n log n)	Splits are roughly balanced on average.
Worst	O(n²)	Pivot always smallest or largest, causing unbalanced splits.
Reflection Questions

What happens if the array is already sorted and you always pick the first element as pivot? If the array is already sorted and you always pick the first element, you get worst-case O(n²).

How could you improve pivot selection to avoid worst-case performance? Improve pivot selection by using a random pivot or median-of-three method.

How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)? Bubble sort: O(n²) average and worst case. Much slower than quicksort for large inputs. Merge sort: O(n log n) guaranteed, but requires extra memory. Quicksort: O(n log n) average, O(n²) worst case, but usually faster in practice because it sorts in-place and has good cache performance.

Why do we use array[1:] instead of array when building the less and greater lists? Because the first element is the pivot. If we used array, the pivot would be included again in the partition, causing duplication or incorrect recursion.
