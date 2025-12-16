"""
Sorting Algorithms Implementation
"""


def bubble_sort(arr):
    """
    Bubble Sort - Repeatedly swap adjacent elements if they're in wrong order
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr


def selection_sort(arr):
    """
    Selection Sort - Find minimum element and place it at beginning
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: No
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr):
    """
    Insertion Sort - Build sorted array one item at a time
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


def merge_sort(arr):
    """
    Merge Sort - Divide and conquer sorting algorithm
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Quick Sort - Divide and conquer using pivot element
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    Stable: No
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr):
    """
    Heap Sort - Build max heap and extract elements
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    Stable: No
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """Helper function to maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr):
    """
    Counting Sort - Non-comparison based sorting for integers
    Time Complexity: O(n + k) where k is range of input
    Space Complexity: O(k)
    Stable: Yes
    Works only for non-negative integers
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] to contain actual position
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


# Example usage and comparison
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_array)
    print("\nSorting Algorithm Results:")
    print("=" * 50)
    
    print("Bubble Sort:   ", bubble_sort(test_array))
    print("Selection Sort:", selection_sort(test_array))
    print("Insertion Sort:", insertion_sort(test_array))
    print("Merge Sort:    ", merge_sort(test_array))
    print("Quick Sort:    ", quick_sort(test_array))
    print("Heap Sort:     ", heap_sort(test_array))
    print("Counting Sort: ", counting_sort(test_array))
    
    # Performance comparison with larger array
    import time
    import random
    
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    print("\n" + "=" * 50)
    print("Performance Comparison (1000 elements):")
    print("=" * 50)
    
    algorithms = [
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
    ]
    
    for name, func in algorithms:
        start = time.time()
        func(large_array)
        end = time.time()
        print(f"{name:15} {(end - start) * 1000:.2f} ms")
