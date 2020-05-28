def sortByBits(arr: list) -> list:
    # return sorted(arr, key=lambda x: (bin(x).count('1'),x))
    def jj(st):
        return bin(st).count('1')
    arr.sort()
    return sorted(arr, key=lambda x: jj(x))

print(sortByBits([0,1,2,3,4,5,6,7,8]))