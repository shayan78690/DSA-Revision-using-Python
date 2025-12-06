class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def printCLL(self):
        if not self.head:
            print("Linked List is Empty")
            return
        
        temp = self.head
        while True:
            print(temp.data, end = " -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("None")
    
    def insertAtBeginning(self, data):
        newnode = Node(data)
        
        if not self.head:
            self.head = newnode
            self.tail = newnode
            newnode.next = self.head
            return
        
        newnode.next = self.head
        self.head = newnode
        self.tail.next = self.head
    
    def insertAtEnding(self, data):
        newnode = Node(data)
        
        if not self.head:
            self.head = newnode
            self.tail = newnode
            newnode.next = self.head
            return
        
        self.tail.next = newnode
        self.tail = newnode
        self.tail.next = self.head
    
    def deleteAtBeginning(self):
        if not self.head:
            print("List is Empty")
            return
        if self.head == self.tail:
            print(f"Deleted Node is {self.head.data}")
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.tail.next = self.head
        
    def deleteAtEnding(self):
        if not self.head:
            print("List is Empty")
            return
        if self.head == self.tail:
            print(f"Deleted Node is {self.head.data}")
            self.head = None
            self.tail = None
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = self.head
        self.tail = temp
        
        
cll = CircularLL()

cll.insertAtBeginning(10)
cll.insertAtEnding(20)
cll.insertAtEnding(30)
cll.printCLL()  
cll.deleteAtBeginning()
cll.deleteAtEnding()
cll.printCLL()
