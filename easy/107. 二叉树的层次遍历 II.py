class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> list:
    if root is None:
        return []
    ans = []
    queue = list()
    queue.append(root)
    while queue:
        temp = []
        for _ in range(len(queue)):
            t = queue.pop(0)
            temp.append(t.val)
            if t.left is not None: queue.append(t.left)
            if t.right is not None: queue.append(t.right)
        ans.append(temp)
    return ans[::-1]