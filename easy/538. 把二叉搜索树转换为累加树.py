from functools import lru_cache
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cnt = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        """递归
        @lru_cache(0)
        def helper(root: TreeNode):
            if not root:
                return root
            if root.right:
                helper(root.right)
            root.val += self.cnt
            self.cnt = root.val
            if root.left:
                helper(root.left)
            return root
        return helper(root)
        """
        stack=[]
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            tmp.val += self.cnt
            self.cnt = tmp.val
            cur = tmp.left
        return root