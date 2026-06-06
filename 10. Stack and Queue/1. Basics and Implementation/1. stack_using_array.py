class Stack:
    def __init__(self):
        self.stack = []   # using Python list as an array
    
    # Push element into stack
    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data} into stack")
    
    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        return self.stack.pop()
    
    # Peek (return top element without removing)
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]
    
    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Display all elements
    def display(self):
        print("Stack elements:", self.stack)

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()          # Output: [10, 20, 30]
    print("Top element:", s.peek())   # Output: 30
    print("Popped element:", s.pop()) # Output: 30
    s.display()          # Output: [10, 20]
