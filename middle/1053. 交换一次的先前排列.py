def prevPermOpt1(A: list) -> list:
    n = len(A)
    for i in range(n-1, 0, -1):
        if A[i - 1] > A[i]:
            break
    mark = i - 1
    max_ = -1
    for j in range(i, n):
        if A[j] < A[i-1]:
            if max_ < A[j]:
                max_ = A[j]
                mark = j
    A[i], A[mark] = A[mark], A[i]
    return A
             
