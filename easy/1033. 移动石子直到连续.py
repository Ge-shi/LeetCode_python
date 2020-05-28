def numMovesStones(a: int, b: int, c: int) -> list:
    x = min(a, b, c)
    z = max(a, b, c)
    y = a + b + c - x - y
    if y - x <= 1 and z - y <= 1:
        return [0, 0]
    if y - x <= 2 or z - y <= 2:
        return [1, z-y+y-x-2]
    else:
        return [2, z-y+y-x-2]