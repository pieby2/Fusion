"""
Common Array Problems and Solutions
"""


def two_sum(nums, target):
    """
    Find two numbers that add up to target
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def maximum_subarray(nums):
    """
    Kadane's Algorithm - Find maximum sum subarray
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
    """
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def find_missing_number(nums):
    """
    Find missing number in array from 0 to n
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: nums = [3, 0, 1] -> 2
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def rotate_array(nums, k):
    """
    Rotate array to the right by k steps
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: nums = [1, 2, 3, 4, 5], k = 2 -> [4, 5, 1, 2, 3]
    """
    k = k % len(nums)
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    
    return nums


def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    
    Example: arr1 = [1, 3, 5], arr2 = [2, 4, 6] -> [1, 2, 3, 4, 5, 6]
    """
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


def find_duplicates(nums):
    """
    Find all duplicates in array (elements range from 1 to n)
    Time Complexity: O(n)
    Space Complexity: O(1) - modifies input array
    
    Example: nums = [4, 3, 2, 7, 8, 2, 3, 1] -> [2, 3]
    """
    result = []
    
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    
    # Restore array
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    
    return result


def product_except_self(nums):
    """
    Return array where each element is product of all elements except itself
    Time Complexity: O(n)
    Space Complexity: O(1) - output array doesn't count
    
    Example: nums = [1, 2, 3, 4] -> [24, 12, 8, 6]
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Calculate right products and multiply
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result


def container_with_most_water(heights):
    """
    Find two lines that form container with most water
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: heights = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
    """
    max_area = 0
    left, right = 0, len(heights) - 1
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, width * height)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def three_sum(nums):
    """
    Find all unique triplets that sum to zero
    Time Complexity: O(n²)
    Space Complexity: O(1) - excluding output
    
    Example: nums = [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
    
    return result


def longest_consecutive_sequence(nums):
    """
    Find length of longest consecutive elements sequence
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: nums = [100, 4, 200, 1, 3, 2] -> 4 (sequence: [1, 2, 3, 4])
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


# Example usage
if __name__ == "__main__":
    print("=== Array Problems Solutions ===\n")
    
    # Two Sum
    print("1. Two Sum:")
    print("   Input: [2, 7, 11, 15], target = 9")
    print("   Output:", two_sum([2, 7, 11, 15], 9))
    
    # Maximum Subarray
    print("\n2. Maximum Subarray (Kadane's Algorithm):")
    print("   Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]")
    print("   Output:", maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    
    # Missing Number
    print("\n3. Find Missing Number:")
    print("   Input: [3, 0, 1]")
    print("   Output:", find_missing_number([3, 0, 1]))
    
    # Rotate Array
    print("\n4. Rotate Array:")
    print("   Input: [1, 2, 3, 4, 5], k = 2")
    print("   Output:", rotate_array([1, 2, 3, 4, 5], 2))
    
    # Merge Sorted Arrays
    print("\n5. Merge Sorted Arrays:")
    print("   Input: [1, 3, 5], [2, 4, 6]")
    print("   Output:", merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
    
    # Product Except Self
    print("\n6. Product Except Self:")
    print("   Input: [1, 2, 3, 4]")
    print("   Output:", product_except_self([1, 2, 3, 4]))
    
    # Container With Most Water
    print("\n7. Container With Most Water:")
    print("   Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]")
    print("   Output:", container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    
    # Three Sum
    print("\n8. Three Sum:")
    print("   Input: [-1, 0, 1, 2, -1, -4]")
    print("   Output:", three_sum([-1, 0, 1, 2, -1, -4]))
    
    # Longest Consecutive Sequence
    print("\n9. Longest Consecutive Sequence:")
    print("   Input: [100, 4, 200, 1, 3, 2]")
    print("   Output:", longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
