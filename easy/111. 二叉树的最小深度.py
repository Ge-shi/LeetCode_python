class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""递归实现"""
def minDepth(root: TreeNode) -> int:
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    min_depth = 2**32
    if root.left:
        min_depth = min(min_depth, minDepth(root.left))
    if root.right:
        min_depth = min(min_depth,minDepth(root.right))
    return min_depth+1


"""BFS"""
def minDepth2(root: TreeNode) -> int:
    if not root:
        return 0
    queue = [(1, root)]
    while queue:
        depth, tmp = queue.pop(0)
        if tmp.left is None and tmp.right is None:
            return depth
        if tmp.left:
            queue.append((depth+1, tmp.left))
        if tmp.right:
            queue.append((depth+1, tmp.right))


"""BFS"""
def minDepth3(root: TreeNode) -> int:
    if not root:
        return 0
    stack = [(1, root)]
    min_depth = float('inf')
    while stack:
        depth, tmp = stack.pop()
        if not tmp.left and not tmp.right:
            min_depth = min(min_depth, depth)
        if tmp.left:
            stack.append((depth + 1, tmp.left))
        if tmp.right:
            stack.append((depth + 1, tmp.right))
    return min_depth