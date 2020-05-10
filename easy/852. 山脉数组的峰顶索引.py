def peakIndexInMountainArray(A: list) -> int:
    n = len(A)
    left = 0
    right = n-1
    print(right)
    while right>left:
        mid = (left + right) // 2
        print("mid", mid)
        if A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
            left = mid
            print("left", left)
        if A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
            right = mid
            print("right", right)
        elif A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
            print("iyiiyi", mid)
            return mid
    print(right)
    return left

nums = [3,4,5,1]
print(peakIndexInMountainArray(nums))