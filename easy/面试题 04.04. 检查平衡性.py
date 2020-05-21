# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
def isBalanced(root: TreeNode) -> bool:
    if not None:
        return True
    return abs(getHeight(root.left) - getHeight(root.right)) < 2 and isBalanced(root.left) and isBalanced(root.right)
def getHeight(root: TreeNode) -> int:
    if not None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1    
"""
def isBalanced(root: TreeNode) -> bool:
    return recur(root) != -1

def recur(root: TreeNode) -> int:
    if not root:
        return 0
    left = recur(root.left)
    if left == -1:
        return -1
    right = recur(root.right)
    if right == -1:
        return -1
    return max(left, right) + 1 if abs(left - right) < 2 else -1