"""
Title     : 1389. Create Target Array in the Given Order
Category  : Array
URL       : https://leetcode.com/problems/create-target-array-in-the-given-order/
submission: https://leetcode.com/submissions/detail/426836618/
"""

from typing import List

# --------------------------------------------------
# Solution:

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result

