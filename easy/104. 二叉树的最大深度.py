class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""递归实现"""
def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    max_depth = -1
    if root.left:
        max_depth = max(max_depth, maxDepth(root.left))
    if root.right:
        max_depth = max(max_depth, maxDepth(root.right))
    return max_depth + 1


"""BFS实现"""
def maxDepth1(root: TreeNode) -> int:
    if not root:
        return 0
    queue = [(1, root)]
    max_depth = -1
    while queue:
        depth, tmp = queue.pop(0)
        if not tmp.left and not tmp.right:
            max_depth = max(max_depth, depth)
        if tmp.left:
            queue.append((depth + 1, tmp.left))
        if tmp.right:
            queue.append((depth + 1, tmp.right))
    return max_depth



"""DFS实现"""
def maxDepth2(root: TreeNode) -> int:
    if root is None:
        return 0
    stack = [(1, root)]
    max_depth = -1
    while stack:
        depth, tmp = stack.pop()
        if not tmp.left and not tmp.right:
            max_depth = max(max_depth, depth)
        if tmp.left:
            stack.append((depth + 1, tmp.left))
        if tmp.right:
            stack.append((depth + 1, tmp.right))
    return max_depth
