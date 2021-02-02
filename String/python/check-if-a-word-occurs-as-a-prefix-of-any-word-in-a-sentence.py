"""
Title     : 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
Category  : String
URL       : https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
submission: https://leetcode.com/submissions/detail/446521260/
"""


# --------------------------------------------------
# Solution:
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, el in enumerate(sentence.split(' '), 1):
            if el.startswith(searchWord):
                return i
        return -1



