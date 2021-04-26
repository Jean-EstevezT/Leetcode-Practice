"""
Title     : 1773. Count Items Matching a Rule
Category  : Array
URL       : https://leetcode.com/problems/count-items-matching-a-rule/
submission: https://leetcode.com/submissions/detail/485543586/
"""

from typing import List
# --------------------------------------------------
# Solution:
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == "type":
                count += 1 if ruleValue == i[0] else 0
            elif ruleKey == "color":
                count += 1 if ruleValue == i[1] else 0
            else:
                count += 1 if ruleValue == i[2] else 0
        return count

