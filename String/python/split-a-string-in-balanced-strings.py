"""
Title     : 1221. Split a String in Balanced Strings
Category  : String
URL       :https://leetcode.com/problems/split-a-string-in-balanced-strings/
submission: https://leetcode.com/submissions/detail/460588791/
"""


# --------------------------------------------------
# Solution:
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            else:
                r += 1

            if l != 0 and l == r:
                total += 1
                l = r = 0
        return total

