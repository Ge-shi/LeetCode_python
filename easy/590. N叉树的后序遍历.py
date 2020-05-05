import sys
sys.path.append("D:\\github\\LeetCode_python")
from Utilities.Tree import MNode

def postorder(root: MNode) -> list:
    res = []
    if root is None:
        return res

    def posOrder(root):
        if root is None:
            return
        childrens = root.children
        for child in childrens:
            posOrder(child)
        res.append(root.val)
    posOrder(root)
    return res

def postorder2(root: MNode) -> list:
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        childrens = node.children
        for child in childrens:
            if child:
                stack.append(child)
    return res[::-1]