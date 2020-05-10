def maximalSquare(matrix: list) -> int:
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return 0
    row, cloumn = len(matrix), len(matrix[0])
    print(row, cloumn)
    maxSide = 0
    dp = [[0 for i in range(cloumn +  1)] for j in range(row + 1)]
    print(dp)
    for i in range(row):
        for j in range(cloumn):
            if matrix[i][j] == 1:
                dp[i + 1][j + 1] = min(min(dp[i + 1][j], dp[i][j + 1]), dp[i][j]) + 1
                maxSide = max(dp[i + 1][j + 1], maxSide)
                print(maxSide)
    return maxSide*maxSide


nums = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(maximalSquare(nums))