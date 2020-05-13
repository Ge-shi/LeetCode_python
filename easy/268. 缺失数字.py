def missingNumber(nums: list) -> int:
    n = len(nums)
    return n*(n+1)/2 - sum(nums)