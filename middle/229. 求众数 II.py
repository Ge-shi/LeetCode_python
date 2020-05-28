class Solution:
    def majorityElement(self, nums: list) -> list:
        """超时
        res = set()
        n = len(nums)
        for elem in nums:
            if nums.count(elem) > n // 3:
                res.add(elem)
        return list(res)
        """
        """空间复杂度O(n)
        n = len(nums)
        mp = {}
        res = set()
        for x in nums:
            # print(mp)
            same = mp.get(x,0)
            if same > n // 3 - 1:
                res.add(x)
            mp[x] = same + 1
            # print(mp)
        return list(res)
        """
        res = []
        n = len(nums)
        candNum1, candNum2 = 0, 0
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if nums[i] == candNum1:
                cnt1 += 1
                continue
            if nums[i] == candNum2:
                cnt2 += 1
                continue
            if cnt1 == 0:
                cnt1 += 1
                candNum1 = nums[i]
                continue
            if cnt2 == 0:
                cnt2 += 1
                candNum2 = nums[i]
            cnt1 -= 1
            cnt2 -= 1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == candNum1:
                cnt1 += 1
            elif num == candNum2:
                cnt2 += 1
        if cnt1 > n // 3:
            res.append(candNum1)
        if cnt2 > n // 3:
            res.append(candNum2)
        return res
    

    print(majorityElement(None,[1,1,1,3,3,2,2,2]))