def findDuplicates(nums: list) -> list:
    res = []
    for i in range(len(nums)):
        j = abs(nums[i])-1
        if nums[j] < 0:
            res.append(j + 1)
        else:
            nums[j] *= -1
    print(nums)
    return res

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))