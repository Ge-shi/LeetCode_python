class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    def helper(l: TreeNode, r: TreeNode):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        if l.val == r.val:
            return helper(l.left, r.right) and helper(l.right, r.left)
        else:
            return False
    if root is None:
        return True
    else:
        return helper(root.left, root.right)