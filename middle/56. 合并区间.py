class Solution:
    def merge(self, intervals: list) -> list:
        res = []
        n = len(intervals)
        if n == 0:
            return res
        intervals.sort()
        first = True
        for left, right in intervals:
            if first or left > res[-1][1]:
                res.append([left,right])
                first = False
            else:
                res[-1][1] = max(res[-1][1], right)
        return res