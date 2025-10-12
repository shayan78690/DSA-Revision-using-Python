class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")
    
    def insertAtBeginning(self, data):
        newnode = Node(data)
        newnode.next = self.head
        if self.head:
            self.head.prev = newnode
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
        newnode.prev = current
    
    
    def deleteAtBeginning(self):
        if not self.head:
            print(f"Linked list is empty")
            return
        if not self.head.next:
            print(f"Deleted node is {self.head.data}")
            return
        self.head = self.head.next
        self.head.prev = None
        
    def deleteAtEnding(self):
        if not self.head:
            print(f"Linked list is empty")
            return
        if not self.head.next:
            print(f"Deleted node is {self.head.data}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None
        
dll = DoublyLinkedList()
dll.insertAtEnd(5)
dll.insertAtEnd(10)
dll.insertAtEnd(15)
dll.insertAtEnd(20)
dll.insertAtEnd(25)
dll.insertAtBeginning(2)
dll.print()
dll.deleteAtBeginning()
dll.deleteAtEnding()
dll.print()