class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
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
        count = 0
        newnode = Node(data)
        current = self.head
        while current and count < index - 1:
            current = current.next
            count += 1
        if not current:
            print("Index out of range.")
            return
        newnode.next = current.next
        current.next = newnode
    
    def deleteAtBeginning(self):
        if not self.head:
            print("Linked List is Empty")
            return
        print(f"Deleted node is {self.head.data}")
        self.head = self.head.next
    
    def deleteAtEnd(self):
        if not self.head:
            print("Linked List is Empty")
            return 
        if not self.head.next:
            print(f"Deleted node is {self.head.data}")
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        print(f"Deleted node: {temp.next.data}")
        temp.next = None
        
    def deleteAtIndex(self, index):
        if not self.head:
            print("List is empty.")
            return
        if index == 0:
            print(f"Deleted node at index 0: {self.head.data}")
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        if not temp or not temp.next:
            print("Index out of range.")
            return
        print(f"Deleted node at index {index}: {temp.next.data}")
        temp.next = temp.next.next
    
    def findLength(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count
    
    def searchElement(self, element):
        temp = self.head
        index = 0
        while temp:
            if temp.data == element:
                return index
            temp = temp.next
            index += 1
        return -1

# 🔹 Test
ll = SinglyLinkedList()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(40)
ll.insertAtIndex(30, 2)
ll.insertAtBeginning(5)
ll.printLL()

# Test delete functions
ll.deleteAtBeginning()
ll.deleteAtEnd()
ll.deleteAtIndex(1)
ll.printLL()
print(ll.findLength())
print(ll.searchElement(30))
