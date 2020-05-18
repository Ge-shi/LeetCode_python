def rob(nums: list) -> int:
    def myRob(lsts: list):
        cur, pre = 0, 0
        for lst in lsts:
            cur, pre = max(pre + lst, cur), cur
        return cur
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    return max(myRob(nums[1:]), myRob(nums[:-1]))


