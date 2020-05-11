def moveZeroes(nums: list) -> None:
    """会使位置次序改变
    left = 0
    right = len(nums) - 1
    print(nums)
    while right > left:
        if nums[left] != 0 and right > left:
            left += 1
        if nums[right] == 0 and right > left:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
    print(nums)
    """
    """下面的不会"""
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1

strs = [0,1,0,3,12]
moveZeroes(strs)
print(strs)