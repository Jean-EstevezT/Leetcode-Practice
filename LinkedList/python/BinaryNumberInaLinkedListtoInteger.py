"""
Title     : 1290. Convert Binary Number in a Linked List to Integer
Category  : Linked List
URL       : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
submission: https://leetcode.com/submissions/detail/427216036/
"""

from typing import List

# --------------------------------------------------
# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        node = 0
        while (temp):
            node += 1
            temp = temp.next
        result = 0
        for i in range(node):
            result += head.val * 2 ** (node - 1 - i)
            head = head.next
        return result

