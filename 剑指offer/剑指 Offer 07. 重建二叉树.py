# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        def helper(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
            if preorder_left > preorder_right:
                return None
            preorder_root = preorder_left
            inorder_root = inorder.index(preorder[preorder_root])
            root = TreeNode(preorder[preorder_root])
            size_left_subTree = inorder_root - inorder_left
            root.left = helper(preorder_left + 1, preorder_left + size_left_subTree, inorder_left, inorder_root - 1)
            root.right = helper(preorder_left + size_left_subTree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)
