class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:        # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head   # Maintain circular link

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:    # Only one node
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.tail.next = self.head

    # Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:    # One node only
            self.head = None
            self.tail = None
            return

        temp = self.head
        while temp.next != self.tail:  # Find second last node
            temp = temp.next

        temp.next = self.head
        self.tail = temp

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# ---------------------------
# TEST THE CIRCULAR LINKED LIST
# ---------------------------

cll = CircularLinkedList()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()        # 10 20 30

cll.insert_at_beginning(5)
cll.display()        # 5 10 20 30

cll.delete_from_beginning()
cll.display()        # 10 20 30

cll.delete_from_end()
cll.display()        # 10 20

