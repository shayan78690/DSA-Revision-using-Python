class Queue:
    def __init__(self):
        self.queue = []   # using Python list as an array

    # Enqueue (add element at the end)
    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued {data} into queue")

    # Dequeue (remove element from the front)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue.")
            return None
        return self.queue.pop(0)   # remove first element

    # Peek (see the front element)
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display all elements
    def display(self):
        print("Queue elements:", self.queue)


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()              # Output: [10, 20, 30]
    print("Front element:", q.peek())   # Output: 10
    print("Dequeued element:", q.dequeue())  # Output: 10
    q.display()              # Output: [20, 30]
