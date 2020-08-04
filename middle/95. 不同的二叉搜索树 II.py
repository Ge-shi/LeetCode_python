# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import functools
class Solution:
    def generateTrees(self, n: int) -> list:
        if n == 0:
            return []
        @functools.lru_cache(None)
        def helper(l: int, r: int):
            res = []
            if l > r:
                res.append(None)
            for i in range(l, r + 1):
                for lo in helper(1, i):
                    for hi in helper(i + 1, r + 1):
                        cur = TreeNode(i)
                        cur.left = lo
                        cur.right = hi
                        res.append(cur)
            return res
        return helper(1,n)