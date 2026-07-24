# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def dfs(self, root, result):
        if not root:
            result.append("N")
            return
        result.append(str(root.val))
        self.dfs(root.left, result)
        self.dfs(root.right, result)
    
    def func(self, values):
        if values[self.index] == "N":
            self.index += 1
            return None
        node = TreeNode(int(values[self.index]))
        self.index += 1
        node.left = self.func(values)
        node.right = self.func(values)
        return node

    def serialize(self, root):
        result = []
        self.dfs(root, result)
        return ",".join(result)
        

    def deserialize(self, data):
        values = data.split(",")
        self.index = 0
        return self.func(values)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
