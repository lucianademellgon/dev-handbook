# Merge Sort
# Logic: Divide & Conquer. Recursively split list in half until lists have size 1. Then merge sorted sublists back together.
# Pros: Guaranteed $O(n \log n)$, Stable.
# Cons: Uses $O(n)$ extra space (not in-place).

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L) # Recursive call
        merge_sort(R)

        i = j = k = 0
        # Merge process
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Check for remaining elements
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1
