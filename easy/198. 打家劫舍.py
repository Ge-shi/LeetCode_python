def rob(nums: list) -> int:
    # n = len(nums)
    # if n == 1:
    #     return nums[0]
    # if n == 0:
    #         return 0
    # dp = [0]*n
    # dp[0] = nums[0]
    # dp[1] = max(nums[0], nums[1])
    # for i in range(2, n):
    #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    # return dp[n-1]
    """
    cur, pre = 0, 0
    for num in nums:
        cur, pre = max(pre + num, cur), cur
    return cur
    """
    even, odd = 0, 0
    n = len(nums)
    for i in range(n):
        if i % 2 == 0:
            even += nums[i]
            even = max(even, odd)
        else:
            odd += nums[i]
            odd = max(odd, even)
    return max(odd, even)

list1 = []
print(rob(list1))