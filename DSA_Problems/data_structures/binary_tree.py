"""
Binary Search Tree Implementation
Time Complexity:
    - Insert: O(log n) average, O(n) worst
    - Search: O(log n) average, O(n) worst
    - Delete: O(log n) average, O(n) worst
Space Complexity: O(n)
"""


class TreeNode:
    """Node class for binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """Insert a node into the BST"""
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for recursive insertion"""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data):
        """Search for a node in the BST"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper method for recursive search"""
        if node is None or node.data == data:
            return node is not None
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)
    
    def inorder_traversal(self):
        """Inorder traversal (Left -> Root -> Right)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Preorder traversal (Root -> Left -> Right)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for preorder traversal"""
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Postorder traversal (Left -> Right -> Root)"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for postorder traversal"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def find_min(self):
        """Find minimum value in BST"""
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self):
        """Find maximum value in BST"""
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def height(self):
        """Calculate height of the tree"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method for calculating height"""
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)
    
    def delete(self, data):
        """Delete a node from BST"""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Helper method for recursive deletion"""
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Get inorder successor (smallest in right subtree)
            min_larger_node = self._find_min_node(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data)
        
        return node
    
    def _find_min_node(self, node):
        """Find node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert elements
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        bst.insert(elem)
    
    print("Inorder Traversal:", bst.inorder_traversal())
    print("Preorder Traversal:", bst.preorder_traversal())
    print("Postorder Traversal:", bst.postorder_traversal())
    
    # Search
    print("\nSearch 40:", bst.search(40))
    print("Search 100:", bst.search(100))
    
    # Min and Max
    print("\nMin value:", bst.find_min())
    print("Max value:", bst.find_max())
    
    # Height
    print("Tree height:", bst.height())
    
    # Delete
    bst.delete(30)
    print("\nAfter deleting 30:", bst.inorder_traversal())
