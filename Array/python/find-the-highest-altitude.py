"""
Title     : 1732. Find the Highest Altitude
Category  : Array
URL       : https://leetcode.com/problems/find-the-highest-altitude/
submission: https://leetcode.com/submissions/detail/448236176/
"""

from typing import List
from itertools import accumulate
# --------------------------------------------------
# Solution:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = list(accumulate(gain)) + [0]
        return max(res)

