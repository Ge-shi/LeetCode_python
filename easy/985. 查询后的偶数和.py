def sumEvenAfterQueries(A: list, queries: list) -> list:
    B = []
    temp = 0
    for x in A:
        if x%2 == 0:
            temp += x 
    for val, index in queries:
        if A[index] & 1 == 0:
            temp -= A[index]
        A[index] += val
        if A[index] & 1 == 0:
            temp += A[index] 
        B.append(temp)
    return B


list1 = [1, 2, 3, 4]
list2 = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(sumEvenAfterQueries(list1, list2))