# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root: TreeNode) -> TreeNode:
    """
    if not root:
        return None
    l = root.left
    r = root.right
    root.left = r
    root.right = l
    invertTree(root.left)
    invertTree(root.right)
    return root
    """
    queue = [root]
    while queue:
        cur = queue.pop(0)
        tmp = cur.left
        cur.left = cur.right
        cur.right = tmp
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return root