"""
Title     : 53. Maximum Subarray
Category  : Array
URL       : https://leetcode.com/problems/maximum-subarray/
submission: https://leetcode.com/submissions/detail/444262780/
"""

from typing import List

# --------------------------------------------------
# Solution:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for i in nums[1:]:
            current = max(i, current + i)
            if current > best:
                best = current
        return best


