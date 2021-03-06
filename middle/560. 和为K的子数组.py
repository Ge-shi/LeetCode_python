class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        
        """暴力
        cnt = 0
        n = len(nums)
        for i in range(0, n + 1):
            j = 0
            while i + j < n:
                if sum(nums[j : j + i + 1]) == k:
                    cnt += 1
                j += 1
        return cnt
        """
        """暴力2
        ans = 0
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i, -1, -1):
                total += nums[j]
                if total == k:
                    ans += 1
        return ans
        """
        """
        acc = ans = 0
        dct = {}
        for num in nums:
            acc += num
            if acc == k:
                ans += 1
            if acc - k in dct:
                ans += dct[acc - k]
            if acc in dct:
                dct[acc] += 1
            else:
                dct[acc] = 1
        return ans
        """
        mp = {0:1}
        ans, pre = 0, 0
        for num in nums:
            pre += num
            if pre - k in mp:
                ans += mp[pre-k]
            if pre in mp:
                mp[pre] += 1
            else:
                mp[pre] = 1
        return ans

nums1 = [1,2,3,4,5,6,4,8,9]
s = 4
print(Solution.subarraySum(None, nums1, s))