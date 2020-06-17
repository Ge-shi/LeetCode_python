def threeSum(nums: list) -> list:
    ans = []
    length = len(nums)
    if length < 3:
        return ans
    nums.sort()
    for i in range(length):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while right > left:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                ans.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            elif total > 0:
                right -= 1
    return ans
print(threeSum([0,0,1,0]))