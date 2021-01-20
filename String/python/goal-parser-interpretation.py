"""
Title     : 1678. Goal Parser Interpretation
Category  : String
URL       : https://leetcode.com/problems/goal-parser-interpretation/
submission: https://leetcode.com/submissions/detail/445626046/
"""

# --------------------------------------------------
# Solution:
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')




