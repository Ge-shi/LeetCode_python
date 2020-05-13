def minCostClimbingStairs(cost: list) -> int:
    """等填坑"""
    min1, min2 = 0, 0
    for i in range(2, len(cost)+1):
        mincost = min(cost[i-1]+min2, cost[i-2]+min1)
        min1, min2 = min2, mincost
    return mincost


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))