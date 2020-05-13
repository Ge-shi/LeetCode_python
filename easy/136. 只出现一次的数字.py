def singleNumber(nums: list) -> int:
    for x in nums[1:]:
        nums[0] = nums[0] ^ x
    return nums[0]  

numss = [4,8,2,4,2]
print(singleNumber(numss))