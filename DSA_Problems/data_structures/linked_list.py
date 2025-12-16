"""
Linked List Implementation
Time Complexity:
    - Insert at beginning: O(1)
    - Insert at end: O(n)
    - Delete: O(n)
    - Search: O(n)
Space Complexity: O(n)
"""


class Node:
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a node at the end of the list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_node(self, key):
        """Delete the first node with the given key"""
        current = self.head
        
        # If head node holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # Key not found
        if not current:
            return
        
        # Unlink the node
        prev.next = current.next
        current = None
    
    def search(self, key):
        """Search for a node with the given key"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def display(self):
        """Display all nodes in the list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty List"
    
    def length(self):
        """Return the length of the linked list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert elements
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_beginning(0)
    
    print("Linked List:", ll.display())
    print("Length:", ll.length())
    
    # Search
    print("Search 2:", ll.search(2))
    print("Search 5:", ll.search(5))
    
    # Delete
    ll.delete_node(2)
    print("After deleting 2:", ll.display())
    
    # Reverse
    ll.reverse()
    print("After reversing:", ll.display())
