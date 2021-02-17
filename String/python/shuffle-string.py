"""
Title     : 1528. Shuffle String
Category  : String
URL       : https://leetcode.com/problems/shuffle-string/
submission: https://leetcode.com/submissions/detail/457278094/
"""

from typing import List
# --------------------------------------------------
# Solution:
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None] * len(s)
        for c, i in zip(s, indices):
            res[i] = c
        return "".join(res)



