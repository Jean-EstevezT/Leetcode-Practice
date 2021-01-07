"""
Title     : 1108. Defanging an IP Address
Category  : String
URL       : https://leetcode.com/problems/defanging-an-ip-address/
submission: https://leetcode.com/submissions/detail/439944756/
"""

# --------------------------------------------------
# Solution:
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

