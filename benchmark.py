
import time
import random
import matplotlib.pyplot as plt


def quicksort_non_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  # Last element as pivot
        less = [x for x in arr[:-1] if x <= pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        
        if len(less) == len(arr) -1 or len(greater) == len(arr) - 1: 
            if len(less) > len(greater):
                return less[:-1] + [less[-1], pivot] + greater
            else:
                return less + [pivot, greater[0]] + greater[1:]
        else:
            return quicksort_non_random(less) + [pivot] + quicksort_non_random(greater)


def benchmark_quicksort(arr_sizes):
    best_case_times = []
    worst_case_times = []
    avg_case_times = []
    
    for n in arr_sizes:
        # Best case: Already sorted array
        sorted_arr = list(range(n))
        start = time.time()
        quicksort_non_random(sorted_arr)
        best_case_times.append(time.time() - start)
        
        # Worst case: Reverse sorted array
        reverse_sorted_arr = list(range(n, 0, -1))
        start = time.time()
        quicksort_non_random(reverse_sorted_arr)
        worst_case_times.append(time.time() - start)
        
        # Average case: Random array
        random_arr = [random.randint(0, n) for _ in range(n)]
        start = time.time()
        quicksort_non_random(random_arr)
        avg_case_times.append(time.time() - start)
    
    return best_case_times, worst_case_times, avg_case_times


array_sizes = [10**2, 10**3, 10**4, 10**5]


best_times, worst_times, avg_times = benchmark_quicksort(array_sizes)


plt.plot(array_sizes, best_times, label='Best Case (Sorted Array)', marker='o')
plt.plot(array_sizes, worst_times, label='Worst Case (Reverse Sorted Array)', marker='o')
plt.plot(array_sizes, avg_times, label='Average Case (Random Array)', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Quicksort Non-Random Pivot Performance')
plt.legend()
plt.xscale('log')  # Logarithmic scale for better clarity on large inputs
plt.yscale('log')
plt.show()