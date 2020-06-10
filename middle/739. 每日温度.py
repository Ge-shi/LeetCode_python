def dailyTemperatures(T: list) -> list:
    res = [0] * len(T)
    stack = []
    for index, elem in enumerate(T):
        # print(index)
        while stack and T[stack[-1]] < elem:
            tmp = stack.pop()
            res[tmp] = index - tmp
        stack.append(index)
    return res
    