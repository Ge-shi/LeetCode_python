# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode:
    """递归
    if root is None or p is None:
        return None
    if p.val >= root.val:
        return inorderSuccessor(root.right, p)
    else:
        l = inorderSuccessor(root.left, p)
        return l if l else root
    """
    if p.right:
        p = p.right
        while p.left:
            p = p.left
        return p
    res = None
    while p != root:
        if p.val > root.val:
            root = root.right
        else:
            res = root
            root = root.left
    return res