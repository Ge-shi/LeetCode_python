# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from functools import lru_cache
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        @lru_cache(0)
        def helper(node: TreeNode):
            if node == None:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            self.ans = max(self.ans, l + r + node.val)
            return max(0, max(r,l) + node.val)
        helper(root)
        return self.ans 
        #     if node == None:
        #         return 0
        #     return node.val + helper(node.left) + helper(node.right)
        # if root == None:
        #     return 0
        # self.ans = max(0, helper(root), self.ans)
        # if root.left != None:
        #     self.ans = max(0, self.ans, self.maxPathSum(root.left))
        # if root.right != None:
        #     self.ans = max(0, self.ans, self.maxPathSum(root.right))
        # return self.ans