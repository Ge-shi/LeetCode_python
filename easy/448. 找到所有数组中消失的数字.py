def findDisappearedNumbers(nums: list) -> list:
    """
    res = []
    dt = {}
    for x in nums:
        dt[x] = 1
    # print(dt)
    for num in range(1, len(nums) + 1):
        if num not in dt:
            res.append(num)
    return res
    """
    res = []
    for x in nums:
        if nums[abs(x)-1] > 0:
            nums[abs(x)-1] *= -1
    print(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))