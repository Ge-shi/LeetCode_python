INT_MAX = 2**31 - 1
INT_MIN = -2**31


def myAtoi(str1: str) -> int:
    left = 0
    right = 0
    if str1 == "":
        return 0
    if str1.isspace():
        return 0
    if str1[0] == ' ' or (str1[0] >= '0' and str1[0] <= '9') or str1[0] == '+' or str1[0] == '-':
        for i in range(len(str1)):
            if str1[i] == '+' or str1[i] == '-' or (str1[i] >= '0' and str1[i] <= '9'):
                print("ceshi")
                left = i
                break
            elif str1[i] != ' ':
                return 0
        k = -1
        print(i)
        if str1[i] == '-' or str1[i] == '+':
            i += 1
        for j in range(i, len(str1)):
            if str1[j] > '9' or str1[j] < '0':
                print("ceshi1", j)
                k = 1
                right = j
                break
        if k == -1:
            right = len(str1)
        print(left, right)
        if left == right - 1 and (str1[left] == '-' or str1[left] == '+'):
            print("chengg")
            return 0
        print(str1[left: right])
        temp = int(str1[left: right])
        if temp > 2**31 - 1:
            temp = 2**31 - 1
        if temp < - 2**31:
            temp = - 2**31
        return temp
    return 0


def myAtoi2(str1: str) -> int:
    res = 0
    i = 0
    flag = 1
    while str1[i] == ' ':
        print(i, "hhu")
        i += 1
    if str1[i] == '-':
        flag = 0
    if str1[i] == '+' or str1[i] == '-':
        print(i)
        i += 1
    while i < len(str1) and str1[i].isdigit():
        r = int(str1[i])
        print(r)
        if res > INT_MAX // 10 or (res == INT_MAX // 10 and res > 7):
            return INT_MAX if flag == 1 else INT_MIN
        res = res * 10 + r
        i += 1
    return res if flag == 1 else -res


print(myAtoi2("  -42"))
