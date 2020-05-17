def maxProfit(prices: list) -> int:
    maxP = 0
    minV = float('inf')
    for price in prices:
        minV = min(minV, price)
        maxP = max(maxP, price - minV)
    return maxP

