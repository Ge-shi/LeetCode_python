def runningSum(nums: list) -> list:
    n = len(nums)
    for i in range(1, n):
        nums[i] += nums[i - 1]
    return nums