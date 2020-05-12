class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def averageOfLevels(root: TreeNode) -> list:
    if root is None:
        return []
    ans = []
    queue = list()
    queue.append(root)
    while queue:
        temp = 0
        n = len(queue)
        for _ in range(n):
            t = queue.pop(0)
            temp += t.val
            if t.left is not None: queue.append(t.left)
            if t.right is not None: queue.append(t.right)
        ans.append(temp/n)
    return ans
