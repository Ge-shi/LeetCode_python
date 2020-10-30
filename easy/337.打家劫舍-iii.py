#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return (0,0)
            steal_left, not_steal_left = helper(node.left)
            steal_right, not_steal_right = helper(node.right)
            steal = not_steal_left + not_steal_right + node.val
            not_steal = max(steal_left, not_steal_left) + max(steal_right, not_steal_right)
            return (steal, not_steal)
        steal, notsteal = helper(root)
        return max(steal, notsteal) 
# @lc code=end

