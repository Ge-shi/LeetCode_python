def findDuplicate(nums: list) -> int:
    def getCount(nums: list, left: int, right: int) -> int:
        count = 0
        for x in nums:
            if x >= left and x <= right:
                count += 1
        return count
    
    n = len(nums)
    left = 1
    right = n - 1
    while right >= left:
        middle = left + (right - left) // 2
        cnt = getCount(nums, left, middle)
        if right == left:
            if cnt > 1:
                return middle
            else:
                break
        if cnt > (middle - left + 1):
            right = middle
        else:
            left = middle + 1
    return -1
    """
    n = len(nums)
    left = 1
    right = n - 1
    while left < right:
        mid = (right + left) // 2
        cnt = 0
        for x in nums:
            if x <= mid:
                cnt += 1
        if cnt > mid:
            right = mid
        else:
            left = mid + 1
    return left
    """


a = [2,1,3,4,2]
print(findDuplicate(a))