def kidsWithCandies(candies: list, extraCandies: int) -> list:
    leng = len(candies)
    flag = [False for _ in range(leng)]
    for i in range(leng):
        if candies[i] + extraCandies >= max(candies):
            flag[i] = True
    return flag