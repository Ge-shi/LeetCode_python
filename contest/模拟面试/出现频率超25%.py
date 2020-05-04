def findSpecialInteger(arr: list) -> int:
    n = len(arr)
    st = set(arr)
    for i in st:
        if arr.count(i)/n >= 0.25:
            return i


list1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]
print(findSpecialInteger(list1))