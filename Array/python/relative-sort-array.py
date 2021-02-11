"""
Title     : 1122. Relative Sort Array
Category  : Array
URL       : https://leetcode.com/problems/relative-sort-array/
submission: https://leetcode.com/submissions/detail/454622350/
"""

from typing import List

# --------------------------------------------------
# Solution:
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        key = dict().fromkeys(arr2, 0)
        temp = []
        while arr1:
            n = arr1.pop()
            if n in key:
                key[n] += 1
                continue
            temp.append(n)
        return [el for el, i in key.items() for _ in range(i)] + sorted(temp)

