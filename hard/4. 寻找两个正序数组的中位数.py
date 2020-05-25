def findMedianSortedArrays(nums1: list, nums2: list):
    n, m = len(nums1), len(nums2)
    nums = [None for _ in range(m + n)] 
    print(nums)
    i, j = 0, 0
    t = 0
    while i < n and j < m:
        print(nums1[i], nums2[j])
        if nums1[i] < nums2[j]:
            nums[t] = nums1[i]
            i += 1
        else:
            nums[t] = nums2[j]
            j += 1
        t += 1
        print(nums)
    if i == n:
        nums[t:] = nums2[j:]
    else:
        nums[t:] = nums1[i:]
    if (n + m) % 2 == 0:
        return (nums[(n + m) // 2] + nums[(n + m) // 2 - 1]) / 2
    else:
        return nums[(n + m)//2]


    
a = [2,3,4]
b = [1,5,6]
print(findMedianSortedArrays(a,b))