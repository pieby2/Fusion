"""
Binary Tree and Graph Problems
"""

from collections import deque


class TreeNode:
    """Binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """
    Maximum depth of binary tree
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height
    
    Example: [3,9,20,null,null,15,7] -> 3
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_valid_bst(root):
    """
    Check if binary tree is valid BST
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def level_order_traversal(root):
    """
    Level order traversal (BFS)
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


def invert_tree(root):
    """
    Invert/mirror a binary tree
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


def is_symmetric(root):
    """
    Check if tree is symmetric
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root)


def lowest_common_ancestor(root, p, q):
    """
    Find lowest common ancestor in BST
    Time Complexity: O(h)
    Space Complexity: O(1)
    """
    if not root:
        return None
    
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root


def path_sum(root, targetSum):
    """
    Check if tree has path with given sum
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if not root:
        return False
    
    if not root.left and not root.right:
        return targetSum == root.val
    
    return (path_sum(root.left, targetSum - root.val) or
            path_sum(root.right, targetSum - root.val))


def right_side_view(root):
    """
    Get right side view of tree
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: [1,2,3,null,5,null,4] -> [1,3,4]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result


def serialize_tree(root):
    """
    Serialize tree to string
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not root:
        return "null"
    
    left = serialize_tree(root.left)
    right = serialize_tree(root.right)
    
    return f"{root.val},{left},{right}"


def deserialize_tree(data):
    """
    Deserialize string to tree
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def helper(nodes):
        val = next(nodes)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node
    
    nodes = iter(data.split(','))
    return helper(nodes)


def diameter_of_tree(root):
    """
    Find diameter of tree (longest path between any two nodes)
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    diameter = [0]
    
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        diameter[0] = max(diameter[0], left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    height(root)
    return diameter[0]


def kth_smallest(root, k):
    """
    Find kth smallest element in BST
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    result = []
    
    def inorder(node):
        if not node or len(result) >= k:
            return
        
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result[k - 1] if k <= len(result) else None


def build_tree_from_preorder_inorder(preorder, inorder):
    """
    Build tree from preorder and inorder traversal
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    mid = inorder.index(root_val)
    
    root.left = build_tree_from_preorder_inorder(
        preorder[1:mid + 1],
        inorder[:mid]
    )
    root.right = build_tree_from_preorder_inorder(
        preorder[mid + 1:],
        inorder[mid + 1:]
    )
    
    return root


def flatten_tree(root):
    """
    Flatten tree to linked list (in-place)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not root:
        return
    
    flatten_tree(root.left)
    flatten_tree(root.right)
    
    if root.left:
        rightmost = root.left
        while rightmost.right:
            rightmost = rightmost.right
        
        rightmost.right = root.right
        root.right = root.left
        root.left = None


# Helper function to create tree from array
def create_tree(arr):
    """Create binary tree from array representation"""
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        node = queue.popleft()
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root


# Example usage
if __name__ == "__main__":
    print("=== Tree Problems Solutions ===\n")
    
    # Create sample tree: [3,9,20,null,null,15,7]
    tree = create_tree([3, 9, 20, None, None, 15, 7])
    
    # Max Depth
    print("1. Maximum Depth:")
    print(f"   Tree: [3,9,20,null,null,15,7]")
    print(f"   Depth: {max_depth(tree)}")
    
    # Level Order Traversal
    print("\n2. Level Order Traversal:")
    print(f"   Result: {level_order_traversal(tree)}")
    
    # Create BST: [4,2,7,1,3]
    bst = create_tree([4, 2, 7, 1, 3])
    
    # Valid BST
    print("\n3. Is Valid BST:")
    print(f"   Tree: [4,2,7,1,3]")
    print(f"   Valid: {is_valid_bst(bst)}")
    
    # Diameter
    print("\n4. Diameter of Tree:")
    print(f"   Tree: [3,9,20,null,null,15,7]")
    print(f"   Diameter: {diameter_of_tree(tree)}")
    
    # Right Side View
    print("\n5. Right Side View:")
    view_tree = create_tree([1, 2, 3, None, 5, None, 4])
    print(f"   Tree: [1,2,3,null,5,null,4]")
    print(f"   View: {right_side_view(view_tree)}")
    
    # Kth Smallest
    print("\n6. Kth Smallest in BST:")
    print(f"   Tree: [4,2,7,1,3]")
    print(f"   3rd smallest: {kth_smallest(bst, 3)}")
    
    # Serialize and Deserialize
    print("\n7. Serialize and Deserialize:")
    serialized = serialize_tree(tree)
    print(f"   Serialized: {serialized[:50]}...")
    deserialized = deserialize_tree(serialized)
    print(f"   Deserialized successfully: {deserialized is not None}")
    
    # Path Sum
    print("\n8. Path Sum:")
    path_tree = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2])
    print(f"   Tree: [5,4,8,11,null,13,4,7,2]")
    print(f"   Has path sum 22: {path_sum(path_tree, 22)}")
