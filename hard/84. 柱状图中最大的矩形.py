def largestRectangleArea(heights: list) -> int:
    """超时
    n = len(heights)
    ans = 0
    for i in range(n):
        minHeight = float('inf')
        for j in range(i, n):
            minHeight = min(minHeight, heights[j])
            ans = max(ans, (j - i + 1) * minHeight)
    return ans
    """
    """超时
    n = len(heights)
    ans = 0
    for i in range(n):
        left = right = i
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1
        while right < n and heights[right] >=heights[i]:
            right += 1
        ans = max(ans, (right - left - 1) * heights[i])
        # print(left, right, ans)
    return ans
    """
    """暴力优化 acceptted
    n = len(heights)
    if n == 0:
        return 0
    left_i = [0] * n
    right_i = [0] * n
    left_i[0] = -1
    right_i[-1] = n
    for i in range(1, n):
        tmp = i - 1
        while tmp >= 0 and heights[tmp] >= heights[i]:
            tmp = left_i[tmp]
        left_i[i]= tmp
    for i in range(n - 2, -1, -1):
        tmp = i + 1
        while tmp < n and heights[tmp] >= heights[i]:
            tmp = right_i[tmp]
        right_i[i] = tmp
    res = 0
    for i in range(n):
        res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
    return res
    """
    stack = []
    heights = [0] + heights + [0]
    res = 0
    for i in range(len(heights)):
        #print(stack)
        while stack and heights[stack[-1]] > heights[i]:
            tmp = stack.pop()
            res = max(res, (i - stack[-1] - 1) * heights[tmp])
        stack.append(i)
    return res

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))