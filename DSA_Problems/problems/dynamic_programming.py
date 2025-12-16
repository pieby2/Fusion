"""
Dynamic Programming Problems and Solutions
"""


def fibonacci(n):
    """
    Calculate nth Fibonacci number
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: n=6 -> 8 (sequence: 0, 1, 1, 2, 3, 5, 8)
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def climbing_stairs(n):
    """
    Number of ways to climb n stairs (1 or 2 steps at a time)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: n=3 -> 3 (ways: 1+1+1, 1+2, 2+1)
    """
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def coin_change(coins, amount):
    """
    Minimum number of coins to make up amount
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    
    Example: coins = [1, 2, 5], amount = 11 -> 3 (5+5+1)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def longest_increasing_subsequence(nums):
    """
    Find length of longest increasing subsequence
    Time Complexity: O(n²)
    Space Complexity: O(n)
    
    Example: [10, 9, 2, 5, 3, 7, 101, 18] -> 4 ([2, 3, 7, 101])
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack Problem - Maximum value with weight constraint
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    
    Example: weights=[1,2,3], values=[6,10,12], capacity=5 -> 22
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def longest_common_subsequence(text1, text2):
    """
    Find length of longest common subsequence
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Example: "abcde", "ace" -> 3 (subsequence "ace")
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def edit_distance(word1, word2):
    """
    Minimum edit distance (Levenshtein distance)
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Example: "horse", "ros" -> 3 (horse->rorse->rose->ros)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]


def word_break(s, wordDict):
    """
    Check if string can be segmented into dictionary words
    Time Complexity: O(n² * m) where m is dict lookup time
    Space Complexity: O(n)
    
    Example: s="leetcode", dict=["leet","code"] -> True
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    word_set = set(wordDict)
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]


def house_robber(nums):
    """
    Maximum money you can rob without robbing adjacent houses
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [2,7,9,3,1] -> 12 (rob house 0, 2, 4)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1


def unique_paths(m, n):
    """
    Number of unique paths in m x n grid (can only move right or down)
    Time Complexity: O(m * n)
    Space Complexity: O(n)
    
    Example: m=3, n=7 -> 28
    """
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    
    return dp[n - 1]


def partition_equal_subset_sum(nums):
    """
    Check if array can be partitioned into two equal sum subsets
    Time Complexity: O(n * sum)
    Space Complexity: O(sum)
    
    Example: [1,5,11,5] -> True ([1,5,5] and [11])
    """
    total = sum(nums)
    
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


def decode_ways(s):
    """
    Number of ways to decode a string where A=1, B=2, ..., Z=26
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: "226" -> 3 ("BZ", "VF", "BBF")
    """
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    prev2, prev1 = 1, 1
    
    for i in range(1, n):
        current = 0
        
        # Single digit decode
        if s[i] != '0':
            current += prev1
        
        # Two digit decode
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            current += prev2
        
        prev2, prev1 = prev1, current
    
    return prev1


# Example usage
if __name__ == "__main__":
    print("=== Dynamic Programming Problems ===\n")
    
    # Fibonacci
    print("1. Fibonacci:")
    print(f"   n=10 -> {fibonacci(10)}")
    
    # Climbing Stairs
    print("\n2. Climbing Stairs:")
    print(f"   n=5 -> {climbing_stairs(5)} ways")
    
    # Coin Change
    print("\n3. Coin Change:")
    print(f"   coins=[1,2,5], amount=11 -> {coin_change([1, 2, 5], 11)} coins")
    
    # Longest Increasing Subsequence
    print("\n4. Longest Increasing Subsequence:")
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"   {nums}")
    print(f"   Length: {longest_increasing_subsequence(nums)}")
    
    # 0/1 Knapsack
    print("\n5. 0/1 Knapsack:")
    weights, values, capacity = [1, 2, 3], [6, 10, 12], 5
    print(f"   weights={weights}, values={values}, capacity={capacity}")
    print(f"   Max value: {knapsack_01(weights, values, capacity)}")
    
    # Longest Common Subsequence
    print("\n6. Longest Common Subsequence:")
    text1, text2 = "abcde", "ace"
    print(f"   '{text1}', '{text2}'")
    print(f"   Length: {longest_common_subsequence(text1, text2)}")
    
    # Edit Distance
    print("\n7. Edit Distance:")
    word1, word2 = "horse", "ros"
    print(f"   '{word1}' -> '{word2}'")
    print(f"   Min edits: {edit_distance(word1, word2)}")
    
    # Word Break
    print("\n8. Word Break:")
    s, wordDict = "leetcode", ["leet", "code"]
    print(f"   s='{s}', dict={wordDict}")
    print(f"   Can break: {word_break(s, wordDict)}")
    
    # House Robber
    print("\n9. House Robber:")
    houses = [2, 7, 9, 3, 1]
    print(f"   Houses: {houses}")
    print(f"   Max money: {house_robber(houses)}")
    
    # Unique Paths
    print("\n10. Unique Paths:")
    print(f"   Grid 3x7")
    print(f"   Paths: {unique_paths(3, 7)}")
    
    # Partition Equal Subset Sum
    print("\n11. Partition Equal Subset Sum:")
    nums = [1, 5, 11, 5]
    print(f"   {nums}")
    print(f"   Can partition: {partition_equal_subset_sum(nums)}")
    
    # Decode Ways
    print("\n12. Decode Ways:")
    s = "226"
    print(f"   String: '{s}'")
    print(f"   Ways: {decode_ways(s)}")
