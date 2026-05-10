# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** Ahmed Ajlal
- **Date:** 05/04/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** 
Dynamic programming is a problem-solving method that breaks a large problem into smaller subproblems.
Instead of solving the same subproblem again and again, it stores previous results and reuses them to make the program faster.
This is useful when the problem has repeated calculations.

- **Time complexity:**
The time complexity depends on the specific problem, but dynamic programming is usually much faster than plain recursion.
For many basic dynamic programming problems, the time complexity can be O(n) or O(n × m) depending on the size of the table used.

- **When to use it:** 
 Dynamic programming is useful for optimization problems where the best answer is built from smaller answers.
It is commonly used in problems like the knapsack problem, Fibonacci sequence, shortest paths, scheduling, and finding the best 
combination of choices.

## Test Result.


| Input          | Result | Notes |
|----------------|--------|-------|
|        5       |  5     |The program calculated the 5th Fibonacci number using stored previous values. |
|       10       |  55    |The program reused earlier results instead of recalculating everything.       |
|       20       | 6765   |Dynamic programming made the calculation faster than simple recursion.        |

## Reflection Questions

1. Why is dynamic programming more efficient than simple recursion?
Dynamic programming is more efficient than simple recursion because it avoids repeating the same calculations many
times. Simple recursion may solve the same subproblem again and again, which wastes time. Dynamic programming stores
those answers and reuses them, making the program faster and more organized.
   


## Challenges Encountered
One challenge in this lab was understanding how dynamic programming stores previous results. At first, it was confusing
because it seemed similar to recursion, but I learned that the main difference is saving and reusing answers. After testing
the program with small inputs, I was able to see how the stored values helped reduce repeated work.
