# Bubble Sort
# Logic: repeatedly swap adjacent elements if they are in the wrong order. Large elements "bubble" to the top.
# Use case: educational purposes mostly. Inefficient for large datasets.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
                swapped = True
        if not swapped: break # Optimization: Stop if already sorted
    return arr
