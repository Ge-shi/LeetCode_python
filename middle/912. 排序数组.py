from functools import lru_cache
class Solution:
    def sortArray(self, nums: list) -> list:
        # return sorted(nums)
        @lru_cache(0)
        def helper(nums: list, begin: int, end: int) -> list:
            if begin >= end:
                return nums[begin:end + 1]
            prit = nums[begin]
            left = begin
            right = end
            while right > left:
                while nums[right] >= prit and left < right:
                    right -= 1
                while nums[left] <= prit and left < right:
                    left += 1
                nums[left], nums[right] = nums[right], nums[left]
            nums[begin] = nums[left]
            nums[left] = prit
            helper(nums, begin, left - 1)
            helper(nums, left + 1, end)
            return nums
        return helper(nums, 0, len(nums) - 1)