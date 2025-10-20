# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class
class Queue:
    def __init__(self):
        self.front = None   # Points to the front (head)
        self.rear = None    # Points to the rear (tail)

    # Enqueue (add element at the end)
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:          # If queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Link old rear to new node
            self.rear = new_node       # Update rear pointer
        print(f"Enqueued {data} into queue")

    # Dequeue (remove element from the front)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue.")
            return None
        temp = self.front
        self.front = self.front.next   # Move front pointer
        if self.front is None:         # If queue becomes empty
            self.rear = None
        return temp.data

    # Peek (get front element without removing)
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        temp = self.front
        print("Queue elements (front to rear): ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()               # Output: 10 20 30
    print("Front element:", q.peek())   # Output: 10
    print("Dequeued element:", q.dequeue())  # Output: 10
    q.display()               # Output: 20 30
