def majorityElement(nums: list) -> int:
    # n = len(nums)
    # mp = {-1:0}
    # for x in nums:
    #     print(mp)
    #     same = mp.get(x,0)
    #     if same > n // 2 - 1:
    #         return x
    #     mp[x] = same + 1
    #     # print(mp)
    # return -1
    """
    n = len(nums)
    curNum = nums[0]
    count = 1
    for i in range(1, n):
        if nums[i] == curNum:
            count += 1
        else:
            count -= 1
            if count == 0:
                curNum = nums[i]
                count = 1
    return curNum
    """
    nums.sort()
    # print(nums)
    return nums[len(nums)//2]


print(majorityElement([3,2,3])) 