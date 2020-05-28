class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x^y).count('1')
        """
        xor = x ^ y
        dis = 0
        while xor:
            if xor & 1:
                dis += 1
            xor = xor >> 1
        return dis
        """
        xor = x ^ y
        dis = 0
        while xor:
            dis += 1
            xor = xor & (xor - 1)
        return dis

print(Solution.hammingDistance(None, 1,4))