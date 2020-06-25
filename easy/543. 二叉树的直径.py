# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node: TreeNode) -> int:
            if node == None:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l+r+1)
            return max(l,r) + 1
        depth(root)
        return self.ans - 1