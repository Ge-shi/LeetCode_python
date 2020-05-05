class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class BinaryTree:
    def __init__(self):
        self.__root = None

    def add(self, item):
        """添加元素"""
        node = TreeNode(item)
        if self.__root is None:
            self.__root = node
        else:
            # 核心思想：将头节点加入至队列，先判断左节点，为空则将节点放置左侧；若不为空，判断右节点，为空则放置右节点。若左右都不为空，分别将左右
            # 节点加入至队列尾，再取队列首节点继续上面逻辑
            queue = list()
            queue.append(self.__root)
            while queue:
                cur = queue.pop()
                if cur.lchild is None:
                    cur.lchild = node
                    return
                if cur.rchild is None:
                    cur.rchild = node
                    return
                # 左右都不为空，将左右节点放置队列尾
                queue.append(cur.rchild)
                queue.append(cur.rchild)
