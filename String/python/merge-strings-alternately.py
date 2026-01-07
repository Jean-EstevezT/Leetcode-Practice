class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                new += word1[i]
            if i < len(word2):
                new += word2[i]
        return new

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(sol.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
    # Example 2
    print(sol.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
    # Example 3
    print(sol.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"