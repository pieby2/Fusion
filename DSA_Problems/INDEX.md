# 📑 DSA Problems - Complete Index

This index provides quick access to all data structures, algorithms, and problems in this collection.

## 📊 Data Structures

### Linked Lists
**File:** `data_structures/linked_list.py`
- Singly Linked List implementation
- Operations: Insert, Delete, Search, Reverse
- Time Complexity: O(1) insert at beginning, O(n) for most operations

### Stack
**File:** `data_structures/stack.py`
- Array-based Stack implementation (LIFO)
- Operations: Push, Pop, Peek, IsEmpty
- Applications: Balanced Parentheses, String Reversal
- Time Complexity: O(1) for all operations

### Queue
**File:** `data_structures/queue.py`
- Regular Queue implementation (FIFO)
- Circular Queue with fixed capacity
- Operations: Enqueue, Dequeue, Front, IsEmpty
- Time Complexity: O(1) for all operations

### Binary Search Tree
**File:** `data_structures/binary_tree.py`
- BST implementation with insertion, deletion, search
- Tree traversals: Inorder, Preorder, Postorder
- Operations: Find Min/Max, Calculate Height
- Time Complexity: O(log n) average, O(n) worst case

---

## 🔧 Algorithms

### Sorting Algorithms
**File:** `algorithms/sorting.py`

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|------------|--------------|-------|--------|
| Bubble Sort | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(k) | Yes |

### Searching Algorithms
**File:** `algorithms/searching.py`

| Algorithm | Time (Avg) | Time (Worst) | Space | Requirement |
|-----------|------------|--------------|-------|-------------|
| Linear Search | O(n) | O(n) | O(1) | None |
| Binary Search | O(log n) | O(log n) | O(1) | Sorted array |
| Jump Search | O(√n) | O(√n) | O(1) | Sorted array |
| Interpolation Search | O(log log n) | O(n) | O(1) | Uniform distribution |
| Exponential Search | O(log n) | O(log n) | O(1) | Sorted array |
| Ternary Search | O(log₃ n) | O(log₃ n) | O(log₃ n) | Sorted array |

### Graph Algorithms
**File:** `algorithms/graph_algorithms.py`

| Algorithm | Purpose | Time Complexity | Space |
|-----------|---------|-----------------|-------|
| BFS | Graph traversal | O(V + E) | O(V) |
| DFS | Graph traversal | O(V + E) | O(V) |
| Dijkstra | Shortest path (non-negative weights) | O((V+E) log V) | O(V) |
| Bellman-Ford | Shortest path (negative weights) | O(V × E) | O(V) |
| Floyd-Warshall | All pairs shortest path | O(V³) | O(V²) |
| Topological Sort | DAG ordering | O(V + E) | O(V) |
| Cycle Detection | Find cycles | O(V + E) | O(V) |

---

## 🎯 Problem Solutions

### Array Problems
**File:** `problems/array_problems.py`

1. **Two Sum** - Find two numbers that add to target
   - Time: O(n), Space: O(n)

2. **Maximum Subarray** (Kadane's Algorithm) - Find max sum subarray
   - Time: O(n), Space: O(1)

3. **Find Missing Number** - Missing number in sequence 0 to n
   - Time: O(n), Space: O(1)

4. **Rotate Array** - Rotate array by k positions
   - Time: O(n), Space: O(1)

5. **Merge Sorted Arrays** - Merge two sorted arrays
   - Time: O(n+m), Space: O(n+m)

6. **Find Duplicates** - Find all duplicates in array
   - Time: O(n), Space: O(1)

7. **Product Except Self** - Product of all elements except current
   - Time: O(n), Space: O(1)

8. **Container With Most Water** - Maximum water container
   - Time: O(n), Space: O(1)

9. **Three Sum** - Find triplets that sum to zero
   - Time: O(n²), Space: O(1)

10. **Longest Consecutive Sequence** - Find longest consecutive sequence
    - Time: O(n), Space: O(n)

### String Problems
**File:** `problems/string_problems.py`

1. **Reverse String** - Reverse a string
2. **Is Palindrome** - Check if string is palindrome
3. **Longest Substring Without Repeating** - Find longest unique substring
4. **Longest Common Prefix** - Find common prefix in array of strings
5. **Is Anagram** - Check if two strings are anagrams
6. **Group Anagrams** - Group anagrams together
7. **Longest Palindromic Substring** - Find longest palindrome
8. **String to Integer (atoi)** - Convert string to integer
9. **Valid Parentheses** - Check if parentheses are balanced
10. **Count and Say** - Generate count-and-say sequence
11. **First Unique Character** - Find first non-repeating character
12. **Reverse Words** - Reverse words in string
13. **Is Subsequence** - Check if string is subsequence

### Dynamic Programming Problems
**File:** `problems/dynamic_programming.py`

1. **Fibonacci** - Calculate nth Fibonacci number
2. **Climbing Stairs** - Count ways to climb stairs
3. **Coin Change** - Minimum coins to make amount
4. **Longest Increasing Subsequence** - Find LIS length
5. **0/1 Knapsack** - Maximum value with weight constraint
6. **Longest Common Subsequence** - Find LCS length
7. **Edit Distance** - Minimum edits to transform strings
8. **Word Break** - Check if string can be segmented
9. **House Robber** - Maximum robbery without adjacent houses
10. **Unique Paths** - Count paths in grid
11. **Partition Equal Subset Sum** - Check if array can be partitioned
12. **Decode Ways** - Count ways to decode string

### Tree Problems
**File:** `problems/tree_problems.py`

1. **Maximum Depth** - Find tree depth
2. **Is Valid BST** - Validate binary search tree
3. **Level Order Traversal** - BFS traversal
4. **Invert Tree** - Mirror a binary tree
5. **Is Symmetric** - Check if tree is symmetric
6. **Lowest Common Ancestor** - Find LCA in BST
7. **Path Sum** - Check if path exists with given sum
8. **Right Side View** - Get right side view of tree
9. **Serialize/Deserialize** - Convert tree to/from string
10. **Diameter of Tree** - Find longest path between nodes
11. **Kth Smallest** - Find kth smallest in BST
12. **Build Tree** - Construct tree from traversals
13. **Flatten Tree** - Flatten to linked list

---

## 🚀 Quick Start

### Run Individual Examples
```bash
# Run data structure example
python3 DSA_Problems/data_structures/linked_list.py

# Run algorithm example
python3 DSA_Problems/algorithms/sorting.py

# Run problem solution
python3 DSA_Problems/problems/array_problems.py
```

### Run All Examples
```bash
python3 DSA_Problems/run_examples.py
```

### Import and Use in Your Code
```python
from DSA_Problems import LinkedList, Stack, Queue, BinarySearchTree

# Create and use data structures
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)

stack = Stack()
stack.push(10)

bst = BinarySearchTree()
bst.insert(5)
```

---

## 📚 Resources

### Time Complexity Cheat Sheet
- **O(1)** - Constant: Stack/Queue operations
- **O(log n)** - Logarithmic: Binary search, BST operations
- **O(n)** - Linear: Array traversal, linear search
- **O(n log n)** - Log-linear: Efficient sorting (merge, heap, quick)
- **O(n²)** - Quadratic: Nested loops (bubble, selection, insertion sort)
- **O(2ⁿ)** - Exponential: Recursive Fibonacci, subset problems
- **O(n!)** - Factorial: Permutations

### Space Complexity Guide
- **In-place**: Modifies input, uses O(1) extra space
- **Out-of-place**: Creates new structure, uses O(n) extra space
- **Recursive**: Uses O(h) stack space where h is recursion depth

---

## 🎓 Learning Path

**Beginners:**
1. Start with basic data structures (Stack, Queue, Linked List)
2. Learn basic sorting (Bubble, Selection, Insertion)
3. Practice simple array and string problems

**Intermediate:**
1. Master trees and graphs
2. Learn efficient sorting and searching
3. Tackle dynamic programming basics

**Advanced:**
1. Complex graph algorithms (Dijkstra, Floyd-Warshall)
2. Advanced dynamic programming
3. Optimization problems

---

## 🤝 Contributing

To add new problems or improve existing solutions:
1. Follow the existing code structure
2. Include time/space complexity analysis
3. Add comprehensive documentation
4. Provide example usage
5. Test your implementation

---

*Happy Coding! 🎉*
