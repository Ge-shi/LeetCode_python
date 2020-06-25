class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return  s1 in s2*2 and len(s1) == len(s2)