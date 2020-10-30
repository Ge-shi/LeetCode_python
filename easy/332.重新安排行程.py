#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dt = collections.defaultdict(list)
        for f,t in tickets:
            dt[f].append(t)
        for f in dt:
            dt[f].sort(reverse=True)
        # print(dt)
        res = []
        def helper(c):
            while dt[c]:
                helper(dt[c].pop())
            res.append(c)
        helper("JFK")
        return res[::-1]
# @lc code=end

