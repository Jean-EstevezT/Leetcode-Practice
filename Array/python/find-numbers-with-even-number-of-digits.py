"""
Title     : 1295. Find Numbers with Even Number of Digits
Category  : Array
URL       : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
submission: https://leetcode.com/submissions/detail/428632729/
"""

from typing import List

# --------------------------------------------------
# Solution:

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        return res


