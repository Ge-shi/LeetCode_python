def firstMissingPositive(nums: list) -> int:
    """
    n = len(nums)
    if n == 0: return 1
    for i in range(1, n + 1):
        if i not in nums:
            return i
    return n + 1
    """
    size = len(nums)
    for i in range(size):
        while nums[i] >= 1 and nums[i] <= size and nums[i] != nums[nums[i] - 1]:
            __swap(nums,i, nums[i] - 1)
    for i in range(size):
        if nums[i] != i+ 1:
            return i + 1
    return size + 1

def __swap(nums: list, i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]


nums = [1,2,0]
print(firstMissingPositive(nums))