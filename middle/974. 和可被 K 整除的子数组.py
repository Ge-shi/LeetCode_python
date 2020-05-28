def subarraysDivByK(A: list, K: int) -> int:
    """wrong
    res = 0
    n = len(A)
    for i in range(2*n - 1):
        left = i // 2
        right = left + i % 2
        while left >= 0 and right < n and (A[left] + A[right]) % K == 0:
            left -= 1
            right += 1
            res += 1
    return res
    """
    """超时
    res = 0
    n = len(A)
    for i in range(n):
        for j in range(i, -1, -1):
            if sum(A[j:i+1]) % K == 0:
                res += 1
    return res
    """
    record = {0: 1}
    total, ans = 0, 0
    for elem in A:
        total += elem
        modulus = total %K
        same = record.get(modulus, 0)
        ans += same
        record[modulus] = same + 1
    return ans 

A = [4,5,0,-2,-3,1]
K = 5
print(subarraysDivByK(A,K))