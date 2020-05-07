def containsDuplicate(nums: list) -> bool:
        return len(nums)!=len(set(nums))


st = [1,2,3,4,5,67,8]
print(containsDuplicate(st))
st1 = [1,2,3,4,6,5,3,5,6]
print(containsDuplicate(st1))
