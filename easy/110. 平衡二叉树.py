class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""自顶向下
def isBalanced(root: TreeNode) -> bool:
    if root == None:
        return True
    return abs(getDepth(root.left) - getDepth(root.right)) < 2 and isBalanced(root.left) and isBalanced(root.right)
    

def getDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return max(getDepth(root.left), getDepth(root.right)) + 1
"""
"""自底向上"""
def isBalanced(root: TreeNode) -> bool:
    return recur(root) != -1


def recur(root: TreeNode):
    if not root:
        return 0
    left = recur(root.left)
    if left == -1:
        return -1
    right = recur(root.right)
    if right == -1:
        return -1
    return max(left, right) + 1 if abs(left - right) < 2 else -1