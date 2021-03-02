"""
Title     : 728. Self Dividing Numbers
Category  : Math
URL       : https://leetcode.com/problems/self-dividing-numbers/
submission: https://leetcode.com/submissions/detail/462766803/
"""

from typing import List

# --------------------------------------------------
# Solution:
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            numb = str(i)
            flag = True
            if '0' not in numb:
                for n in numb:
                    if i % int(n) != 0:
                        flag = False
                        break
                if flag:
                    res.append(i)
        return res


