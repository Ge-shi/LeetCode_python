import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if re.match(p+'$',s) else False