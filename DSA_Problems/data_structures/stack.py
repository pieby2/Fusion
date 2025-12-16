"""
Stack Implementation (LIFO - Last In First Out)
Time Complexity:
    - Push: O(1)
    - Pop: O(1)
    - Peek: O(1)
    - IsEmpty: O(1)
Space Complexity: O(n)
"""


class Stack:
    """Stack implementation using Python list"""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item from stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        """Return number of items in stack"""
        return len(self.items)
    
    def display(self):
        """Display stack contents"""
        return str(self.items)


def is_balanced_parentheses(expression):
    """
    Check if parentheses in expression are balanced
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def reverse_string(s):
    """
    Reverse a string using stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("Stack:", stack.display())
    print("Size:", stack.size())
    print("Peek:", stack.peek())
    
    # Pop elements
    print("Pop:", stack.pop())
    print("After pop:", stack.display())
    
    # Test balanced parentheses
    test_cases = [
        "((()))",
        "({[]})",
        "(()",
        "([)]"
    ]
    
    print("\nBalanced Parentheses Tests:")
    for test in test_cases:
        print(f"{test}: {is_balanced_parentheses(test)}")
    
    # Test string reversal
    print("\nString Reversal:")
    print(f"Original: 'hello'")
    print(f"Reversed: '{reverse_string('hello')}'")
