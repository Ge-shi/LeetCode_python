# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """递归
        if not root:
            return False
        sum -= root.val
        if root.left is None and root.right is None:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        """
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            node, curNum = stack.pop()
            if node.left is None and node.right is None and curNum == 0:
                return True
            if node.left:
                stack.append([node.left, curNum - node.left.val])
            if node.right:
                stack.append([node.right, curNum - node.right.val])
        return False