from functools import lru_cache
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root: TreeNode, sum_: int) -> int:
    @lru_cache(0)
    def countPath(root: TreeNode, sum_: int):
        if not root:
            return 0
        sum_ -= root.val
        result = 1 if sum_ == 0 else 0
        return result + countPath(root.left, sum_) + countPath(root.right, sum_)
    if root == None:
        return 0
    a = countPath(root, sum_)
    b = countPath(root.left, sum_)
    c = countPath(root.right, sum_)
    return a + b + c