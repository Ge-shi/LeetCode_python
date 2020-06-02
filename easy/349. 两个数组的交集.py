def intersection(nums1: list, nums2: list) -> list:
    return list(set(nums1).intersection(set(nums2)))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))