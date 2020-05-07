class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    flag = False
    if s is not None and t is not None:
        if s.val == t.val:
            flag = subTree(s, t)
        if flag == False:
            flag = isSubtree(s.left, t)
        if flag == False:
            flag = isSubtree(s.right, t)

    def subTree(pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # if pRoot2 is None:
        #     return True
        # if pRoot1 is None:
        #     return False
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return subTree(pRoot1.left, pRoot2.left) & subTree(pRoot1.right, pRoot2.right)

    return flag

    
    