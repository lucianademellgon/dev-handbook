# Quick Sort
# Logic: Select a Pivot. 
# Partition the array so elements $< pivot$ are on left, and $> pivot$ are on right. 
# Recursively sort parts.Pros: Generally fastest in practice (good cache locality). In-place (mostly).Cons: Worst case $O(n^2)$ if pivot is bad (e.g., picking 1st element in sorted list). 
# Solution: Pick random pivot.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] # Middle element strategy
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
