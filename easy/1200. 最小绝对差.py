def minimumAbsDifference(arr: list) -> list:
    res = []
    arr.sort()
    min_diff = float('inf')
    n = len(arr)
    for i in range(n-1):
        min_diff = min(min_diff, arr[i + 1] - arr[i])
    for i in range(n - 1):
        if arr[i + 1] - arr[i] == min_diff:
            res.append([arr[i], arr[i + 1]])
    return res    