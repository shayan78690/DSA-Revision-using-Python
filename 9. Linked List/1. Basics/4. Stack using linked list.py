# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class
class Stack:
    def __init__(self):
        self.top = None   # Top points to the top node of the stack

    # Push element onto the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top   # link new node to current top
        self.top = new_node        # make new node the top
        print(f"Pushed {data} into stack")

    # Pop element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        popped = self.top.data
        self.top = self.top.next   # move top pointer to next node
        return popped

    # Peek (get top element)
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    # Check if stack is empty
    def is_empty(self):
        return self.top is None

    # Display elements of the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        temp = self.top
        print("Stack elements (top to bottom): ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()               # Output: 30 20 10
    print("Top element:", s.peek())    # Output: 30
    print("Popped element:", s.pop())  # Output: 30
    s.display()               # Output: 20 10
