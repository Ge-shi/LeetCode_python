def checkSubarraySum(nums: list, k: int) -> bool:
    """
    if k == 0:
        for i in range(len(nums) - 1):
            if nums[i] + nums[i+1] == 0:
                return True
        return False
    ans, res, pre = 0, 0, 0
    mp = {0:1}
    for elem in nums:
        if elem % k == 0:
            ans += 1
        pre += elem
        modulus = pre % k
        same = mp.get(modulus, 0)
        res += same
        mp[modulus] = same + 1
    return res - ans > 0
    """
    if k == 0:
        for i in range(len(nums) - 1):
            if nums[i] + nums[i+1] == 0:
                return True
        return False
    pre = 0
    mp = {0:1}
    for i in range(len(nums)):
        pre += nums[i]
        modulus = pre % k
        same = mp.get(modulus, -1)
        if i - same > 1:
            return True
        mp[modulus] = i
    return False


nums = [23,2,4,6,7]
k = 100
print(checkSubarraySum(nums, k))