"""
Title     : 1446. Consecutive Characters
Category  : String
URL       : https://leetcode.com/problems/consecutive-characters/
submission: https://leetcode.com/submissions/detail/465321880/
"""


# --------------------------------------------------
# Solution:
class Solution:
    def maxPower(self, s: str) -> int:
        t = 1
        for i in range(len(s) - 1):
            w = s[i]
            if w == s[i + 1]:
                n = 1
                for j in s[i + 1:]:
                    if j != w:
                        break
                    n += 1
                t = t if t > n else n
        return t


