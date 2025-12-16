"""
Queue Implementation (FIFO - First In First Out)
Time Complexity:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Front: O(1)
    - IsEmpty: O(1)
Space Complexity: O(n)
"""


class Queue:
    """Queue implementation using Python list"""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item from queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def size(self):
        """Return number of items in queue"""
        return len(self.items)
    
    def display(self):
        """Display queue contents"""
        return str(self.items)


class CircularQueue:
    """
    Circular Queue implementation using fixed-size array
    More efficient than regular queue for fixed capacity
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front == -1
    
    def is_full(self):
        """Check if queue is full"""
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, item):
        """Add item to circular queue"""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
    
    def dequeue(self):
        """Remove and return front item from circular queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.items[self.front]
        
        if self.front == self.rear:  # Only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        return item
    
    def get_front(self):
        """Return front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front]
    
    def size(self):
        """Return number of items in queue"""
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - self.front + self.rear + 1
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            return "[]"
        
        result = []
        i = self.front
        while True:
            result.append(str(self.items[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        
        return "[" + ", ".join(result) + "]"


# Example usage
if __name__ == "__main__":
    # Regular Queue
    print("=== Regular Queue ===")
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print("Queue:", queue.display())
    print("Size:", queue.size())
    print("Front:", queue.front())
    
    print("Dequeue:", queue.dequeue())
    print("After dequeue:", queue.display())
    
    # Circular Queue
    print("\n=== Circular Queue ===")
    cq = CircularQueue(5)
    
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    
    print("Circular Queue:", cq.display())
    print("Size:", cq.size())
    
    print("Dequeue:", cq.dequeue())
    print("After dequeue:", cq.display())
    
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    
    print("After more enqueues:", cq.display())
    print("Is Full:", cq.is_full())
