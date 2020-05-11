def removeDuplicates(nums: list) -> int:
    # nums = set(nums)
    # print(nums)
    # return len(nums)
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[cnt]:
            cnt += 1
            nums[cnt] = nums[i]
    print(nums[:cnt+1])
    return cnt + 1



nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))