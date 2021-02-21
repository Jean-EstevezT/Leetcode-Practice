"""
Title     : 1636. Sort Array by Increasing Frequency
Category  : Array
URL       : https://leetcode.com/problems/sort-array-by-increasing-frequency/
submission: https://leetcode.com/submissions/detail/458942482/
"""

from typing import List
from collections import Counter
# --------------------------------------------------
# Solution:
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        tp = Counter(nums)
        return sorted(nums, key=lambda x: (-tp[x], x), reverse=True)

