"""
Title     : 1323. Maximum 69 Number
Category  : Math
URL       : https://leetcode.com/problems/maximum-69-number/
submission: https://leetcode.com/submissions/detail/449430549/
"""

# --------------------------------------------------
# Solution:
class Solution:
    def maximum69Number (self, num: int) -> int:
        res = num
        n = [*str(num)]
        for i in range(len(n)):
            n[i] = '6' if n[i] == '9' else '9'
            res = max(res, int(''.join(n)))
            n = [*str(num)]
        return res


