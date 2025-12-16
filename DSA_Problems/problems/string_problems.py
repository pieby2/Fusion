"""
Common String Problems and Solutions
"""


def reverse_string(s):
    """
    Reverse a string
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "hello" -> "olleh"
    """
    return s[::-1]


def is_palindrome(s):
    """
    Check if string is palindrome (ignoring non-alphanumeric)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: "A man, a plan, a canal: Panama" -> True
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def longest_substring_without_repeating(s):
    """
    Find length of longest substring without repeating characters
    Time Complexity: O(n)
    Space Complexity: O(min(n, m)) where m is charset size
    
    Example: "abcabcbb" -> 3 (substring "abc")
    """
    char_set = set()
    left = max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


def longest_common_prefix(strs):
    """
    Find longest common prefix among array of strings
    Time Complexity: O(S) where S is sum of all characters
    Space Complexity: O(1)
    
    Example: ["flower", "flow", "flight"] -> "fl"
    """
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


def is_anagram(s, t):
    """
    Check if two strings are anagrams
    Time Complexity: O(n)
    Space Complexity: O(1) - limited to 26 characters
    
    Example: "anagram", "nagaram" -> True
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True


def group_anagrams(strs):
    """
    Group anagrams together
    Time Complexity: O(n * k log k) where k is max string length
    Space Complexity: O(n * k)
    
    Example: ["eat", "tea", "tan", "ate", "nat", "bat"] 
             -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    anagram_groups = {}
    
    for string in strs:
        sorted_str = ''.join(sorted(string))
        if sorted_str not in anagram_groups:
            anagram_groups[sorted_str] = []
        anagram_groups[sorted_str].append(string)
    
    return list(anagram_groups.values())


def longest_palindromic_substring(s):
    """
    Find longest palindromic substring
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Example: "babad" -> "bab" or "aba"
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = end = 0
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)      # Odd length palindrome
        len2 = expand_around_center(i, i + 1)  # Even length palindrome
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]


def string_to_integer(s):
    """
    Convert string to integer (atoi)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: "   -42" -> -42
    """
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    index = 0
    
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        index = 1
    
    result = 0
    
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1
    
    result *= sign
    
    # Clamp to 32-bit integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if result > INT_MAX:
        return INT_MAX
    if result < INT_MIN:
        return INT_MIN
    
    return result


def valid_parentheses(s):
    """
    Check if parentheses are valid and properly closed
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "()[]{}" -> True, "([)]" -> False
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    
    return len(stack) == 0


def count_and_say(n):
    """
    Generate nth term of count-and-say sequence
    Time Complexity: O(2^n)
    Space Complexity: O(2^n)
    
    Example: n=4 -> "1211"
    Sequence: 1, 11, 21, 1211, 111221, ...
    """
    if n == 1:
        return "1"
    
    prev = count_and_say(n - 1)
    result = []
    i = 0
    
    while i < len(prev):
        char = prev[i]
        count = 1
        
        while i + 1 < len(prev) and prev[i + 1] == char:
            count += 1
            i += 1
        
        result.append(str(count) + char)
        i += 1
    
    return ''.join(result)


def first_unique_character(s):
    """
    Find first non-repeating character in string
    Time Complexity: O(n)
    Space Complexity: O(1) - limited to 26 characters
    
    Example: "leetcode" -> 0 (character 'l')
    """
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1


def reverse_words(s):
    """
    Reverse words in a string
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "  hello world  " -> "world hello"
    """
    words = s.split()
    return ' '.join(reversed(words))


def is_subsequence(s, t):
    """
    Check if s is subsequence of t
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: s = "abc", t = "ahbgdc" -> True
    """
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)


# Example usage
if __name__ == "__main__":
    print("=== String Problems Solutions ===\n")
    
    # Palindrome
    print("1. Is Palindrome:")
    test_str = "A man, a plan, a canal: Panama"
    print(f"   Input: '{test_str}'")
    print(f"   Output: {is_palindrome(test_str)}")
    
    # Longest Substring Without Repeating
    print("\n2. Longest Substring Without Repeating:")
    test_str = "abcabcbb"
    print(f"   Input: '{test_str}'")
    print(f"   Output: {longest_substring_without_repeating(test_str)}")
    
    # Longest Common Prefix
    print("\n3. Longest Common Prefix:")
    test_arr = ["flower", "flow", "flight"]
    print(f"   Input: {test_arr}")
    print(f"   Output: '{longest_common_prefix(test_arr)}'")
    
    # Anagram
    print("\n4. Is Anagram:")
    s1, s2 = "anagram", "nagaram"
    print(f"   Input: '{s1}', '{s2}'")
    print(f"   Output: {is_anagram(s1, s2)}")
    
    # Group Anagrams
    print("\n5. Group Anagrams:")
    test_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"   Input: {test_arr}")
    print(f"   Output: {group_anagrams(test_arr)}")
    
    # Longest Palindromic Substring
    print("\n6. Longest Palindromic Substring:")
    test_str = "babad"
    print(f"   Input: '{test_str}'")
    print(f"   Output: '{longest_palindromic_substring(test_str)}'")
    
    # String to Integer
    print("\n7. String to Integer (atoi):")
    test_str = "   -42"
    print(f"   Input: '{test_str}'")
    print(f"   Output: {string_to_integer(test_str)}")
    
    # Valid Parentheses
    print("\n8. Valid Parentheses:")
    test_cases = ["()[]{}", "([)]"]
    for test in test_cases:
        print(f"   Input: '{test}' -> {valid_parentheses(test)}")
    
    # Count and Say
    print("\n9. Count and Say:")
    print(f"   n=4 -> '{count_and_say(4)}'")
    
    # First Unique Character
    print("\n10. First Unique Character:")
    test_str = "leetcode"
    print(f"   Input: '{test_str}'")
    print(f"   Output: {first_unique_character(test_str)}")
    
    # Reverse Words
    print("\n11. Reverse Words:")
    test_str = "  hello world  "
    print(f"   Input: '{test_str}'")
    print(f"   Output: '{reverse_words(test_str)}'")
    
    # Is Subsequence
    print("\n12. Is Subsequence:")
    s, t = "abc", "ahbgdc"
    print(f"   Input: s='{s}', t='{t}'")
    print(f"   Output: {is_subsequence(s, t)}")
