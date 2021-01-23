"""
Title     : 1684. Count the Number of Consistent Strings
Category  : String
URL       : https://leetcode.com/problems/count-the-number-of-consistent-strings/
submission: https://leetcode.com/submissions/detail/446521260/
"""

from typing import List

# --------------------------------------------------
# Solution 1:
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            tp = True
            for el in w:
                if el not in allowed:
                    tp = False
                    break
            if tp:
                count += 1
        return count


# Solution 2:
# class Solution:
    # def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
            # if all((el in allowed for el in w)):
                # count += 1
        # return count


