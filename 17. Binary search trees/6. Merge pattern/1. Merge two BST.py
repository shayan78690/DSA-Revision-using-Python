'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def merge(self, root1, root2):
        result = []
        self.inorder(root1, result)
        self.inorder(root2, result)
        result.sort()
        return result
    
    def inorder(self, root, result):
        if not root:
            return 
        self.inorder(root.left, result)
        result.append(root.data)
        self.inorder(root.right, result)



'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def merge(self, root1, root2):
        list1 = []
        list2 = []
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        while i < len(list1):
            result.append(list1[i])
            i += 1
        while j < len(list2):
            result.append(list2[j])
            j += 1
        
        return result
    
    def inorder(self, root, result):
        if not root:
            return 
        self.inorder(root.left, result)
        result.append(root.data)
        self.inorder(root.right, result)
