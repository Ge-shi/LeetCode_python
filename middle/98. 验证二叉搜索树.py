import sys
sys.path.append("D:\\github\\LeetCode_python")
from Utilities.Tree import TreeNode
pre = -2**32

def isValidBST(root: TreeNode) -> bool:
    global pre # 可以定义一个初始化函数，self.pre = None,以后涉及全局变量，可以
    if root == None:
        return True
    if isValidBST(root.left) == False:
        return False
    if pre >= root.val:
        return False
    pre = root.val
    return isValidBST(root.right)

