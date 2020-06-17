def searchRange(nums: list, target: int) -> list:

    def binary_search(nums: list, target: int):
        length = len(nums)
        left, right = 0, length - 1
        while right >= left:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        return -1
    def left_bound(nums: list, target: int):
        length = len(nums)
        if length == 0:
            return -1
        left, right = 0, length - 1
        while right >= left:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        if left < length and nums[left] == target:
            return left
        else:
            return -1
    
    def right_bound(nums: list, target: int):
        length = len(nums)
        if length == 0:
            return -1
        left, right = 0, length - 1
        while right >= left:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                left = middle + 1   
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        if right >= 0 and nums[right] == target:
            return right
        else:
            return - 1
    return [left_bound(nums, target), right_bound(nums, target)]
    """O(n)解法
    n = len(nums)
    if n == 0:
        return [-1, -1]
    for i in range(n):
        if nums[i] == target:
            break
    for j in range(n - 1, -1, -1):
        if nums[j] == target:
            break
    # print(i,j)
    if (i >= n - 1 and nums[i] != target) and (j <= 0 and nums[j] != target):
        return [-1, -1]
    else:
        return [i, j]
    """

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))