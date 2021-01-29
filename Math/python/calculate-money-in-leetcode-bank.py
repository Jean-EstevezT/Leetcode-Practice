"""
Title     : 1716. Calculate Money in Leetcode Bank
Category  : Math
URL       : https://leetcode.com/problems/calculate-money-in-leetcode-bank/
submission: https://leetcode.com/submissions/detail/449492254/
"""

# --------------------------------------------------
# Solution:
class Solution:
    def totalMoney(self, n: int) -> int:
        ttl, flag, add = 0, 0, 0
        cont = 7
        for _ in range(n):
            add += 1
            ttl += add
            cont -= 1
            if cont <= 0:
                flag += 1
                add = flag
                cont = 7
        return ttl

