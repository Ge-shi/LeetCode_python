#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(postorder[0])
        root_val = postorder[-1]
        root  =TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root
# @lc code=end

