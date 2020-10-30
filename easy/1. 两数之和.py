def twoSum(self, nums: list, target: int) -> list:
    hashmap = {}
    for index, num in enumerate(nums):
        hashmap[num] = index
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and j != i:
            return [i, j]


print("hello")
