# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        l = nums[:mid]
        r = nums[mid + 1:]
        node.left = self.sortedArrayToBST(l)
        node.right = self.sortedArrayToBST(r)
        return node