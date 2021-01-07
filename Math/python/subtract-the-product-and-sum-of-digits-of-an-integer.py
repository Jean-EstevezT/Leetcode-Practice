"""
Title     : 1281. Subtract the Product and Sum of Digits of an Integer
Category  : Math
URL       : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
submission: https://leetcode.com/submissions/detail/439934427/
"""

from typing import List

# --------------------------------------------------
# Solution:
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for i in str(n):
            p *= int(i)
            s += int(i)
        return p - s

