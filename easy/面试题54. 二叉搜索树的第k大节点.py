import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # stack = collections.deque()
        # cur = root
        # res = 1
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.right
        #     node = stack.pop()
        #     if res == k:
        #         return node.val
        #     res += 1
        #     cur = node.left
        # return -1
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
