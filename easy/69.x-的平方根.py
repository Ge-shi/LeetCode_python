#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left = 0
        right = x // 2
        while right > left:
            mid = (right - left + 1) // 2 + left
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return right
# @lc code=end

