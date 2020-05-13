def findPairs(nums: list, k: int) -> int:
    if k < 0:
        return 0
    if k == 0:
        return len(set([i for i in nums if nums.count(i) >= 2]))
    if k > 0:
        cl = [i+k for i in nums]
    return len(set(cl)&set(nums))