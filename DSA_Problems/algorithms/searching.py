"""
Searching Algorithms Implementation
"""


def linear_search(arr, target):
    """
    Linear Search - Search by checking each element sequentially
    Time Complexity: O(n)
    Space Complexity: O(1)
    Works on: Sorted and unsorted arrays
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search - Divide and conquer on sorted array
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Works on: Sorted arrays only
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary Search - Recursive implementation
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def jump_search(arr, target):
    """
    Jump Search - Jump ahead by fixed steps then linear search
    Time Complexity: O(√n)
    Space Complexity: O(1)
    Works on: Sorted arrays only
    """
    import math
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Jump to find block where element may be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


def interpolation_search(arr, target):
    """
    Interpolation Search - Improved binary search for uniformly distributed data
    Time Complexity: O(log log n) for uniform distribution, O(n) worst case
    Space Complexity: O(1)
    Works on: Sorted arrays with uniform distribution
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Probing position with better formula
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


def exponential_search(arr, target):
    """
    Exponential Search - Find range then binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Works on: Sorted unbounded/infinite arrays
    """
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find range for binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Binary search in found range
    left = i // 2
    right = min(i, len(arr) - 1)
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def ternary_search(arr, target, left=0, right=None):
    """
    Ternary Search - Divide array into three parts
    Time Complexity: O(log₃ n)
    Space Complexity: O(log₃ n) due to recursion
    Works on: Sorted arrays only
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)


# Example usage and comparison
if __name__ == "__main__":
    # Sorted array for testing
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    
    print(f"Array: {sorted_array}")
    print(f"Target: {target}")
    print("\nSearch Results:")
    print("=" * 50)
    
    result = linear_search(sorted_array, target)
    print(f"Linear Search:        Index {result}")
    
    result = binary_search(sorted_array, target)
    print(f"Binary Search:        Index {result}")
    
    result = binary_search_recursive(sorted_array, target)
    print(f"Binary (Recursive):   Index {result}")
    
    result = jump_search(sorted_array, target)
    print(f"Jump Search:          Index {result}")
    
    result = interpolation_search(sorted_array, target)
    print(f"Interpolation Search: Index {result}")
    
    result = exponential_search(sorted_array, target)
    print(f"Exponential Search:   Index {result}")
    
    result = ternary_search(sorted_array, target)
    print(f"Ternary Search:       Index {result}")
    
    # Test with missing element
    missing_target = 100
    print(f"\n\nSearching for missing element ({missing_target}):")
    print("=" * 50)
    
    result = binary_search(sorted_array, missing_target)
    print(f"Binary Search: {result} (not found)")
    
    # Performance comparison
    import time
    import random
    
    large_sorted_array = sorted([random.randint(1, 10000) for _ in range(10000)])
    search_target = large_sorted_array[len(large_sorted_array) // 2]
    
    print("\n" + "=" * 50)
    print("Performance Comparison (10000 elements):")
    print("=" * 50)
    
    algorithms = [
        ("Linear Search", linear_search),
        ("Binary Search", binary_search),
        ("Jump Search", jump_search),
        ("Interpolation Search", interpolation_search),
        ("Exponential Search", exponential_search),
    ]
    
    for name, func in algorithms:
        start = time.time()
        for _ in range(1000):
            func(large_sorted_array, search_target)
        end = time.time()
        print(f"{name:22} {(end - start) * 1000:.2f} ms")
