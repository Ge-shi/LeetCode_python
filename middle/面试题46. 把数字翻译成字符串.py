def translateNum(num: int) -> int:
    st = str(num)
    a = b = 1
    for i in range(2, len(st) + 1):
        a, b = a + b if "25" >= st[i - 2: i] >= "10" else a, a
    return a

print(translateNum(12258))