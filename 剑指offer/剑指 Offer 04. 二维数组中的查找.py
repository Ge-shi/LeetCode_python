def findNumberIn2DArray(matrix: list, target: int) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    i = 0
    j = n - 1
    while i < m and j >= 0:
        # print(matrix[i][j])
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        elif matrix[i][j] == target:
            return True
    return False
