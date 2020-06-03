from functools import lru_cache
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> list:
        """
        if not root:
            return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if node.left is None and node.right is None and sum(tmp) == sum_:
                res.append(tmp)
            if node.left:
                stack.append([tmp + [node.left.val], node.left])
            if node.right:
                stack.append([tmp + [node.right.val], node.right])
        return res
        """
        def helper(root, tmp, sum_):
            if not root:
                return
            if root.left is None and root.right is None and sum_ - root.val == 0:
                tmp.append(root.val)
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)
        res = []
        helper(root, [], sum_)
        return res