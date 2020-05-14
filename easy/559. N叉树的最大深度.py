class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""DFS"""
def maxDepth(root: 'Node') -> int:
    if not root:
        return 0
    stack = [(1, root)]
    max_depth = -1
    while stack:
        depth, tmp = stack.pop()
        if not tmp.children:
            max_depth = max(max_depth, depth)
        for child in tmp.children:
            if child:
                stack.append((depth + 1, child))
    return max_depth


"""递归实现"""
def maxDepth1(root: 'Node') -> int:
    if not root:
        return 0
    if not root.children:
        return 1
    max_depth = -1
    for child in root.children:
        max_depth = max(max_depth, maxDepth1(child))
    return max_depth + 1


"""BFS"""
def maxDepth2(root: 'Node') -> int:
    if not root:
        return 0
    queue = [root]
    max_depth = 0
    while queue:
        tmp = []
        for _ in range(len(queue)):
            t = queue.pop(0)
            tmp.append(t.val)
            for child in t.children:
                if child:
                    queue.append(child)
        if tmp != []:
            max_depth += 1
    return max_depth
