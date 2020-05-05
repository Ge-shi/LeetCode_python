import sys
sys.path.append("D:\\github\\LeetCode_python")
from Utilities.Tree import TreeNode


def inorderTraversal(root: TreeNode) -> list:
    ans = []
    if root == None:
        return ans
    def middleOrder(root):
        if root == None:
            return
        middleOrder(root.left)
        ans.append(root.val)
        middleOrder(root.right)
    middleOrder(root)
    return ans


def inorderTraversal2(root: TreeNode) -> list:
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        m = stack.pop()
        res.append(m.val)
        cur = m.right
    return res


def inorderTraversal3(root: TreeNode) -> list:
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None: continue
        if color == WHITE:
            stack.append((WHITE,node.right))
            stack.append((GRAY, node))
            stack.append((WHITE, node.left))
        else:
            res.append(node.val)
    return res