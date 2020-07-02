from heapq import *


class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        pq = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                heappush(pq, -matrix[i][j])
                if len(pq) > k:
                    heappop(pq)
        return -pq[0]
