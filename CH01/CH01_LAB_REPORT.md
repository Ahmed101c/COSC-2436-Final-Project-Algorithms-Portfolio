# Chapter X: Introduction to Algorithms — Lab Report

## Student Information
- **Name:** Ahmed Ajlal
- **Date:** 05/01/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:**
- This chapter introduced algorithms as step-by-step instructions for solving problems. The lab compared linear search and binary search. Linear search checks each item one by one, while binary search works on a sorted list by repeatedly cutting the search area in half.
  
- **Time complexity:**
  Linear search has a time complexity of O(n) because it may need to check every item in the list. Binary search has a time complexity of O(log n) because it reduces the search area by half with each step.
  
- **When to use it:**
  Linear search is useful when the list is small or unsorted. Binary search is useful when the list is sorted and large because it finds items much faster than checking every value one by one.


## Test Results
Input	Result	Notes
List: [1, 3, 5, 7, 9], Target: 7	Found	Linear search checked values one by one until it found 7.
List: [1, 3, 5, 7, 9], Target: 7	Found	Binary search found the value by checking the middle area of the sorted list.
List: [1, 3, 5, 7, 9], Target: 4	Not Found	The target value was not in the list.


## Reflection Questions

1. **What did this lab help you understand about algorithms?**
   This lab helped me understand that algorithms are step-by-step methods for solving problems.
   By comparing linear search and binary search, I learned that two algorithms can solve the same problem but perform very
   differently depending on how they are designed. Binary search is much faster for sorted lists because it reduces the search
   area each time instead of checking every item one by one.
  
## Challenges Encountered
One challenge in this lab was understanding the difference between linear search and binary search. At first, both seemed like simple searching methods, but I learned that binary search is more efficient because it divides the list in half each time. I also learned that binary search only works correctly when the list is already sorted, which is an important detail to remember.
