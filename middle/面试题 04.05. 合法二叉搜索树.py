class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode) -> bool:
    pre = -2**32
    def isBST(root: TreeNode) -> bool:
        global pre
        if root is None:
            return True
        if not isBST(root.left):
            return False
        if pre >= root.val:
            return False
        pre = root.val
        return isBST(root.right)
    return isBST(root)
