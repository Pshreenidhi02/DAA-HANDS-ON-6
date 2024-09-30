
import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr) 
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort_random(less) + equal + quicksort_random(greater)

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort_random(arr))
