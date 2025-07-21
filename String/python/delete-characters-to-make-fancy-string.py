"""
Title     : 1957. Delete Characters to Make Fancy String
Category  : String
URL       : https://leetcode.com/problems/delete-characters-to-make-fancy-string/
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for char in s:
            # Check if we already have at least 2 characters 
            # in the result and if the current character is the same as the last two
            if len(res) >= 2 and char == res[-1] and char == res[-2]:
                continue
            res.append(char)
        return "".join(res)