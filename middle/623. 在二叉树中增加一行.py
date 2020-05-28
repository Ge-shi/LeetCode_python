# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        queue = [[root,1]]
        while queue:
            cur, depth = queue.pop(0)
            # print(cur.val, depth)
            if depth == d - 1:
                node1 = TreeNode(v)
                node2 = TreeNode(v)
                node1.left = cur.left
                node2.right = cur.right
                cur.left = node1
                cur.right = node2
            if depth >= d:
                break
            if cur.left:
                queue.append([cur.left, depth + 1])
            if cur.right:
                queue.append([cur.right, depth + 1])
        return root
