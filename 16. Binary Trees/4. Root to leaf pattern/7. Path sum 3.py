class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        return (
            self.func(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )

    def func(self, root, targetSum):
        if not root:
            return 0

        count = 0

        if root.val == targetSum:
            count += 1

        count += self.func(root.left, targetSum - root.val)
        count += self.func(root.right, targetSum - root.val)

        return count
