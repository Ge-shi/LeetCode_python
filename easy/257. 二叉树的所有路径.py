# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from functools import lru_cache
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        # res = []
        # @lru_cache(0)
        # def helper(node: TreeNode, tmp):
        #     if node:
        #         tmp += str(node.val)
        #         if node.left == None and node.right == None:
        #             res.append(tmp)
        #         else:
        #             tmp += "->"
        #             helper(node.left, tmp)
        #             helper(node.right, tmp)
        # helper(root, "")
        # return res
        res = []
        if root == None:
            return res
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                res.append(path)
            if node.right != None:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left != None:
                stack.append((node.left, path + "->" + str(node.left.val)))            
        return res