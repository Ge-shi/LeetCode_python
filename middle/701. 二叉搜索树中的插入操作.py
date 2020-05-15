class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root:
            return node
        pre, pNode = None, root
        while pNode:
            pre = pNode
            if node.val > pNode.val:
                pNode = pNode.right
            else:
                pNode = pNode.left
        if pre.val > node.val:
            pre.left = node
        else:
            pre.right = node 
        return root
        """递归
        node = TreeNode(val)
        if root == None:
            return node
        def insert(root: TreeNode, pNode: TreeNode):
            if root is None:
                return
            if root.val > pNode.val:
                if root.left == None:
                    root.left = pNode
                else:
                    insert(root.left, pNode)
            elif root.val < pNode.val:
                if root.right is None:
                    root.right = pNode
                else:
                    insert(root.right, pNode)
        insert(root, node)
        return root
        """
