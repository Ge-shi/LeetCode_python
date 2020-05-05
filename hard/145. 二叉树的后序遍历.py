import sys
sys.path.append("D:\\github\\LeetCode_python")
from Utilities.Tree import TreeNode

def postorderTraversal(root: TreeNode) -> list:
    res = []
    if root is None:
        return res

    def posOrder(root):
        if root is None:
            return
        posOrder(root.left)
        posOrder(root.right)
        res.append(root.val)
    posOrder(root)
    return res

def postorderTraversal2(root: TreeNode) -> list:
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            res.append(cur.val)
            cur = cur.right
        m = stack.pop()
        cur = m.left
    return res[::-1]
    

def postorderTraversal3(root: TreeNode) -> list:
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None: continue
        if color == WHITE:
            stack.append((GRAY, node))
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)
    return res