
def quicksort_non_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  
        less = [x for x in arr[:-1] if x <= pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return quicksort_non_random(less) + [pivot] + quicksort_non_random(greater)

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort_non_random(arr))
