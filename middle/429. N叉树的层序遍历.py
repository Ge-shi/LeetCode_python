class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: 'Node') -> list:
    if root == None:
        return []
    ans = []
    queue = list()
    queue.append(root)
    while queue:
        temp = []
        for _ in range(len(queue)):
            t = queue.pop(0)
            temp.append(t.val)
            childrens = t.children
            for child in childrens:
                if child:
                    queue.append(child)
        ans.append(temp)
    return ans