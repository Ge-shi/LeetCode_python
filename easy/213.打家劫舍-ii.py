#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(lists):
            cur, pre = 0, 0
            for num in lists:
                cur, pre = max(cur, pre + num), cur
            return cur
        return max(helper(nums[1:]), helper(nums[:-1]))
# @lc code=end

