def numPairsDivisibleBy60(time: list) -> int:
    res = [0] * 60
    for i in time:
        res[i%60] += 1
    cnt = 0
    for i in range(0, 60):
        if res[i] == 0:
            pass
        if i == 0 or i == 30:
            cnt += res[i] * (res[i] - 1)
        else:
            cnt += res[i] * res[60 - i]
    return cnt>>1