"""
Title     : 169. Majority Element
Category  : Array
URL       : https://leetcode.com/problems/majority-element/
submission: https://leetcode.com/submissions/detail/429329104/
"""

from typing import List

# --------------------------------------------------
# Solution:
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

