class Queue:
    def __init__(self):
        self.items = []  
        # Initializes an empty list to hold the queue elements

    def enqueue(self, item):
        # Adds an item to the back of the queue.
        self.items.append(item)

    def dequeue(self):
        # Removes and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        # Returns the item at the front without removing it.
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        # Checks if the queue is empty.
        return len(self.items) == 0

    def size(self):
        # Returns the number of items in the queue.
        return len(self.items)

# Example Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())          # Output: 10
print(queue.peek())             # Output: 20
print(queue.size())             # Output: 2
print(queue.is_empty())         # Output: False
