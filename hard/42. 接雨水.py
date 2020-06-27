class Solution:
    def trap(self, height: list) -> int:
        n = len(height)
        max1, max2 = 0, 0
        s1, s2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n - i - 1] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        return s1 + s2 - n * max1 - sum(height)