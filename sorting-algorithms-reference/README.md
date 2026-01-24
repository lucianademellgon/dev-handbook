# Sorting Algorithms Reference ⚡

## 1. Key Concepts & Definitions
Before analyzing algorithms, define these properties (crucial for exam theory):

* **Stability:** A sorting algorithm is *stable* if two objects with equal keys appear in the same order in sorted output as they appear in the input.
    * *Important for:* Sorting database records (e.g., sort by Date, then by Name).
* **In-Place:** An algorithm is *in-place* if it requires a small, constant amount of extra memory space ($O(1)$ auxiliary space).
* **Divide and Conquer:** Breaking the problem into sub-problems, solving them, and combining results (used in Merge & Quick Sort).

---

## 2. Complexity Cheat Sheet 📊

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable? | Method |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ Yes | Exchanging |
| **Selection Sort**| $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ❌ No | Selection |
| **Insertion Sort**| $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ Yes | Insertion |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$| $O(n \log n)$| $O(n)$ | ✅ Yes | Merging |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$| $O(n^2)$ | $O(\log n)$| ❌ No | Partitioning |

---

## 3. Elementary Sorts ($O(n^2)$)

### 🫧 Bubble Sort
**Logic:** Repeatedly swap adjacent elements if they are in the wrong order. Large elements "bubble" to the top.
* **Use case:** Educational purposes mostly. Inefficient for large datasets.

```python
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
