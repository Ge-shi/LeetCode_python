from functools import lru_cache
class Solution:
    # @lru_cache(100)
    def threeSumClosest(self, nums: list, target: int) -> int:
        n = len(nums)
        if n <= 3:
            return sum(nums)
        nums.sort()
        # print(nums)
        
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n):
            # if nums[i] >= target:
            #     break
            left = i + 1
            right = n -1
            while right > left:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return ans
        return ans