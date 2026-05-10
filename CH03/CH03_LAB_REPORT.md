Lab 3: Recursion

Student Information

Name: Ahmed Ajlal
Date: 02/12/2026
Recursion Concepts

Two Parts of Every Recursive Function

Base Case: The base case is the condition that stops the recursive function from calling itself again. It represents the simplest version of the problem that can be solved directly without further recursion. When the base case is met, the function returns a value immediately, preventing infinite recursion and allowing the call stack to begin unwinding.
Recursive Case: The recursive case is the part of the function where it calls itself to solve a smaller or simpler version of the original problem. Each recursive call reduces the problem size and moves it closer to the base case. Once the base case is reached, the results are returned back through each previous call until the final solution is produced.
The Call Stack

The call stack is a data structure that keeps track of active function calls in a program. Each time a function is called, a new stack frame is added (pushed) onto the top of the stack. This frame stores the function’s parameters, local variables, and the location to return to after the function finishes. When the function completes, its frame is removed (popped) from the stack, and control returns to the previous function. For example, consider factorial(3). The program first calls factorial(3), which then calls factorial(2), which then calls factorial(1). Each of these calls is pushed onto the stack. When factorial(1) reaches the base case and returns 1, that call is popped off the stack. Then factorial(2) resumes, calculates 2 × 1, returns 2, and is popped. Finally, factorial(3) calculates 3 × 2, returns 6, and is popped. The stack grows as recursive calls are made and shrinks as they return, working in a last-in, first-out order.

Function Analysis

Function	Base Case	Recursive Case	Time Complexity
countdown	i <= 0	countdown(i-1)	O(n)
fact	x <= 1	x * fact(x-1)	O(n)
recursive_sum	empty list	first + sum(rest)	O(n)
recursive_count	empty list	1 + count(rest)	O(n)
recursive_max	single item	max(first, max(rest))	O(n)
Reflection Questions

What happens if you forget the base case? If you forget the base case, the recursive function will continue calling itself indefinitely because there is no stopping condition. Each call adds a new frame to the call stack, and eventually the program runs out of stack space. This results in a recursion depth error (such as a RecursionError in Python), and the program crashes without producing a result.

Why is the naive Fibonacci implementation inefficient? The naive recursive Fibonacci function is inefficient because it repeatedly recalculates the same values. For example, to compute fib(5), it calculates fib(4) and fib(3), but fib(4) itself calculates fib(3) and fib(2) again. This leads to many duplicate computations.

Draw the call stack for fact(4). fact(4) └── fact(3) └── fact(2) └── fact(1) ← base case
