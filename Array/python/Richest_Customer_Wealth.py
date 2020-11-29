"""
Title     : 1672. Richest Customer Wealth
Category  : Array
URL       : https://leetcode.com/problems/richest-customer-wealth/
submission: https://leetcode.com/submissions/detail/425399063/
"""

from typing import List

# --------------------------------------------------

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max((sum(i) for i in accounts))

