"""
Title     : 1470. Shuffle the Array
Category  : Array
URL       : https://leetcode.com/problems/shuffle-the-array/
submission: https://leetcode.com/submissions/detail/425788185/
"""

from typing import List

# --------------------------------------------------
# Solution 1:
# class Solution:
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
        # return [item for el in zip(nums[:n], nums[n:]) for item in el]


# Solution 2:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x, y in zip(nums[:n], nums[n:]):
            result.append(x)
            result.append(y)
        return result
