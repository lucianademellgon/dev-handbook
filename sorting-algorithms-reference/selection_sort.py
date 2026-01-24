# Selection Sort
# Logic: Divide list into sorted/unsorted. Find the minimum element in the unsorted part and swap it with the first unsorted element.
# Note: Minimizes the number of swaps (good if write operations are expensive), but always $O(n^2)$.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swap min to front
    return arr
