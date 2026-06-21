class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
    def insertAtBeginning(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def insertAtEnd(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBeginning(data)
            return
        newnode = Node(data)
        count = 0
        current = self.head
        while current and count < index-1:
            current = current.next
            count += 1
        if not current:
            print("Index out of range")
            return

        newnode.next = current.next
        current.next = newnode
    def deleteAtBeginning(self):
        if not self.head:
            print("Linked list is empty")
            return
        print(f"Deleted node is {self.head.data}")
        self.head = self.head.next
    def deleteAtEnd(self):
        if not self.head:
            print("Linked list is empty")
            return
        if not self.head.next:
            print(f"Deleted node is {self.head.data}")
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        print(f"Deleted node is {current.next.data}")
        current.next = None
    def deleteAtIndex(self, index):
        if not self.head:
            print("Linked list is empty")
            return
        if index == 0:
            print(f"Deleted node at index 0: {self.head.data}")
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current and count < index-1:
            current = current.next
            count += 1
        if not current or not current.next:
            print("Index out of range")
            return 
        print(f"Deleted node is {current.next.data}")
        current.next = current.next.next
    def length(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        print(f"Length of the linked list is {count}")
    def searchElement(self, element):
        index = 0
        current = self.head

        while current:
            if current.data == element:
                return index

            current = current.next
            index += 1

        return -1
        
ll = LinkedList()
ll.insertAtBeginning(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.printLL()
ll.insertAtIndex(10, 3)
ll.printLL()
ll.deleteAtIndex(3)
ll.printLL()
ll.deleteAtBeginning()
ll.printLL()
ll.deleteAtEnd()
ll.printLL()
ll.length()
print(ll.searchElement(3))

            
