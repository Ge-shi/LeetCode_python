import sys
sys.path.append("D:\\github\\LeetCode_python")
from Utilities.Tree import TreeNode

def preorderTraversal(root: TreeNode) -> list:
    ans = []
    if root == None:
        return ans
    def preOrder(root):
        if root == None:
            return
        ans.append(root.val)
        preOrder(root.left)
        preOrder(root.right)
    preOrder(root)
    return ans

def preorderTraversal2(root: TreeNode) -> list:
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            res.append(cur.val)
            cur = cur.left
        m = stack.pop()
        cur = m.right
    return res

def preorderTraversal3(root: TreeNode) -> list:
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None: continue
        if color == WHITE:
            stack.append((WHITE,node.right))
            stack.append((WHITE, node.left))
            stack.append((GRAY, node))
        else:
            res.append(node.val)
    return res