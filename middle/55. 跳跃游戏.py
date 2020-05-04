def canJump(nums) -> bool:
    # 如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。
    # 可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。
    # 如果可以一直跳到最后，就成功了。
    n = len(nums)
    farst = 0
    for i in range(n):
        if i > farst:
           return False
        farst = max(farst, nums[i] + i)
    return True


str1 = [2, 3, 1, 1, 4]
print(canJump(str1))
