from typing import List


def countdown(i: int) -> None:
 
    if i <= 0:          
        print(0)
        return
    else:               
        print(i)
        countdown(i - 1)


def fact(x: int) -> int:
  
    if x <= 1:          
        return 1
    else:               
        return x * fact(x - 1)


def recursive_sum(arr: List[int]) -> int:
   
    if not arr:         
        return 0
    else:               
        return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr: List) -> int:
   
    if not arr:         
        return 0
    else:               #
        return 1 + recursive_count(arr[1:])


def recursive_max(arr: List[int]) -> int:
    
    if len(arr) == 1:   
        return arr[0]
    else:               
        rest_max = recursive_max(arr[1:])
        return arr[0] if arr[0] > rest_max else rest_max
