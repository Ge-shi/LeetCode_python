def maxProduct(nums: list) -> int:
    res, imax, imin = -float('inf'), 1, 1
    for x in nums:
        if x < 0:
            imax, imin = imin, imax
        imax = max(imax * x, x)
        imin = min(imin * x, x)
        res = max(res, imax)
    return res


list1 = [2,3,-2,4]
print(maxProduct(list1))