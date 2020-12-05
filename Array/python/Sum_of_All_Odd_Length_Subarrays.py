"""
Title     : 1588. Sum of All Odd Length Subarrays
Category  : Array
URL       : https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
submission: https://leetcode.com/submissions/detail/427512252/
"""

from typing import List

# --------------------------------------------------
# Solution:

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = sum(arr)
        length = len(arr)
        for l in range(2, length + 1):
            if l % 2 != 0:
                for sub in range(length + 1 - l):
                    result += sum(arr[sub:sub + l])
        return result


