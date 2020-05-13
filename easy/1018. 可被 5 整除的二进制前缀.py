def prefixesDivBy5(A: list) -> list:
    num = 0
    for i, dig in enumerate(A):
        num = (dig + num*2)%5
        A[i] = (num%5 == 0)
    return A