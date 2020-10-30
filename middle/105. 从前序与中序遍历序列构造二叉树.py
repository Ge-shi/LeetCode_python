# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder: list, inorder: list) -> TreeNode:
    def helper(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
        if preorder_left > preorder_right:
            return None
        preorder_root = preorder_left
        inorder_root = inorder.index(preorder[preorder_root])
        root = TreeNode(preorder[preorder_root])
        size_left_subtree = inorder_root - inorder_left
        root.left = helper(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
        # 递归地构造右子树，并连接到根节点
        # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
        root.right = helper(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
        return root
    return helper(0, len(preorder) - 1, 0, len(preorder))