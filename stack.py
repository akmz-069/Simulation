class Stack:
    def __init__(self):
        self.items = []
        
    # To append items into the stack
    def push(self, item):
        self.items.append(item)
    # To Remove the items from ths stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        return self.items[-1] if not self.is_empty() else "Stack is empty"
    #checks if the stack is empty 
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())      # Output: 2
print(stack.peek())     # Output: 1
