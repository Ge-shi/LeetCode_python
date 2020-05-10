def maxArea(height: list) -> int:
    n =len(height)
    left = 0
    right = n - 1
    ans = 0
    while right > left:
        if height[left] > height[right]:
            ans = max(ans, height[right]*(right - left))
            right -= 1
        else:
            ans = max(ans, height[left]*(right - left))
            left += 1
    return ans


nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))