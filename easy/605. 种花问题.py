def canPlaceFlowers(flowerbed: list, n: int) -> bool:
    length = len(flowerbed)
    res = 0
    if n <= 0:
        return True
    if length == 1:
        return True if flowerbed[0] == 0 and n <= 1 else False
    if length == 0:
        return False
    for i in range(length):
        print("i ==", i, flowerbed)
        if i == 0:
            if flowerbed[1] == 0 and flowerbed[0] == 0:
                res += 1
                flowerbed[i] = 1
                print(i, flowerbed)
                continue
        if i == length - 1:
            if flowerbed[length - 2] == 0 and flowerbed[length - 1] == 0:
                res += 1
                flowerbed[i] = 1
                continue
        if flowerbed[i] == 0 and flowerbed[i - 1]== 0 and flowerbed[i + 1] == 0:
            res += 1
            flowerbed[i] = 1
    print("res == ", res)
    return True if res >= n else False

f = [0,0]
n = 2
print(canPlaceFlowers(f, n))