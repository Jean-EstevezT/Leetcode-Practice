"""
Title     : 1431. Kids With the Greatest Number of Candies
Category  : Array
URL       : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""

from typing import List

#--------------------------------------------------

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [candie + extraCandies >= greatest for candie in candies]


