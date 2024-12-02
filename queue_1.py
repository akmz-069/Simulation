class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to hold the queue elements

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        """Return the item at the front without removing it."""
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Example Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # Output: 10
print(queue.peek())     # Output: 20
print(queue.size())     # Output: 2
print(queue.is_empty()) # Output: False
