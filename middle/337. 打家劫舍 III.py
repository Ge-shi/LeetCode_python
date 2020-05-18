class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rob(root: TreeNode) -> int:
    """
    if root is None:
        return 0
    money = root.val
    if root.left:
        money += (rob(root.left.left) + rob(root.left.right))
    if root.right:
        money += (rob(root.right.left) + rob(root.right.right))
    return max(money, rob(root.left) + rob(root.right))
    """
    """
    memo = {}
    def myRob(root: TreeNode, memo: dict):
        if root is None:
            return 0
        if root in memo:
            return memo[root]
        money = root.val
        print(money, "money")
        if root.left:
            money += (myRob(root.left.left, memo) + myRob(root.left.right, memo))
        if root.right:
            money += (myRob(root.right.left, memo) + myRob(root.right.right,memo))
        result = max(money, myRob(root.left, memo) + myRob(root.right, memo))
        print(result, "result")
        memo.update({root:result})
        return result
    return myRob(root, memo)
    """
    def dp(node):
        #返回值是偷取该节点和不偷取该节点的最大收益
        if node == None:
            return (0,0)
        steal_left,not_steal_left = dp(node.left)
        steal_right,not_steal_right = dp(node.right)
        steal = not_steal_left + not_steal_right + node.val
        not_steal = max(steal_left,not_steal_left) + max(steal_right,not_steal_right)
        return (steal,not_steal)
    steal,not_steal = dp(root)
    return max(steal,not_steal)
