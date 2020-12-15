"""
Title     : 1351. Count Negative Numbers in a Sorted Matrix
Category  : Array
URL       : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
submission: https://leetcode.com/submissions/detail/430992626/
"""

from typing import List

# --------------------------------------------------
# Solution:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([n for el in grid for n in el if n < 0])

