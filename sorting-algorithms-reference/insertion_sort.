# Insertion Sort
# Logic: Build the sorted array one item at a time. 
# Pick an element and shift previous elements right until the correct spot is found (like sorting cards in hand).
# Use case: Extremely efficient for small data or nearly sorted data.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
