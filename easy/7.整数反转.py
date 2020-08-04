#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        t = abs(x)
        while t != 0:
            t, y = divmod(t, 10)
            if res > 2147483647 // 10 or (res == 2147483647 // 10 and y > 7):
                return 0
            res = res * 10 + y
        if x > 0:
            return res
        else:
            if res <= 2147483648:
                return -res
            else:
                return 0
# @lc code=end
