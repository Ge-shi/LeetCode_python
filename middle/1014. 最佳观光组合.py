def maxScoreSightseeingPair(A: list) -> int:
    n = len(A)
    mx = A[0] + 0
    ans = 0
    for i in range(1, n):
        ans = max(ans, mx + A[i] - i)
        mx = max(mx, A[i] + i)
    return ans

A = [8,1,5,2,6]
print(maxScoreSightseeingPair(A))