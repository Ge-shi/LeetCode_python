def canThreePartsEqualSum(A: list) -> bool:
    sumA = sum(A)
    if sumA%3 != 0:
        return False
    part = sumA/3
    cur = cnt = 0
    for x in A:
        cur += x
        if cnt == 2:
            return True
        if cur == part:
            cur = 0
            cnt += 1
    return False