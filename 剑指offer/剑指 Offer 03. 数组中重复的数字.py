def findRepeatNumber(nums: list) -> int:
    dt={}
    for elem in nums:
        if elem not in dt:
            dt[elem] = 1
        else:
            return elem
    return -1
