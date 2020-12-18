"""
Title     : 1. Two Sum
Category  : Array
URL       : https://leetcode.com/problems/two-sum/
submission: https://leetcode.com/submissions/detail/432056558/
"""

from typing import List

# --------------------------------------------------
# Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                d = nums[i] + nums[j]
                if d == target:
                    return [i, j]

