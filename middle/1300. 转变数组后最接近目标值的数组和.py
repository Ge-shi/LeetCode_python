def findBestValue(arr: list, target: int) -> int:
    # sorted(arr)
    # n = len(arr)
    # minDif = abs(arr[0] * n - target)
    # ans = 0
    # for i in range(1, n):
    #     tmp = abs(sum(arr[:i]) + (n - i) * arr[i] - target)
    #     if tmp < minDif:
    #         minDif = tmp
    #         ans = i
    # return arr[ans]
    arr.sort()
    s,n=0,len(arr)
    for i in range(len(arr)):
        avg=(target-s)/(n-i)
        if avg<arr[i]:
            return int(avg+0.4999999)   #五舍六入
        s+=arr[i]
    return arr[-1]
