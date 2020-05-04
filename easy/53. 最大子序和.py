def maxSubArray(nums) -> int:
    n = len(nums)
    ans = 0
    total = 0
    for i in range(1, n):
        if total >= 0:
            total += nums[i]
        else:
            total = nums[i]
        if ans < total:
            ans = total
    return ans


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums1))
