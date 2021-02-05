"""
Title     : 1309. Decrypt String from Alphabet to Integer Mapping
Category  : String
URL       : https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
submission: https://leetcode.com/submissions/detail/452162190/
"""


# --------------------------------------------------
# Solution:
from string import ascii_lowercase

class Solution:
    def freqAlphabets(self, s: str) -> str:
        for n in range(26, -1, -1):
            if 9 < n:
                s = s.replace(str(n) + '#', ascii_lowercase[n - 1])
            else:
                s = s.replace(str(n), ascii_lowercase[n - 1])
        return s

