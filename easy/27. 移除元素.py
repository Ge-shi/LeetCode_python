def removeElement(nums: list, val: int) -> int:
    cnt = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[cnt] = nums[i]
            cnt += 1
    print(nums[:cnt])
    return cnt


nums = [0,1,2,2,3,0,4,2]
val = 3
print(removeElement(nums, val))