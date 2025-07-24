"""
Title     : 1695. Maximum Erasure Value
Category  : Array
URL       : https://leetcode.com/problems/maximum-erasure-value/
"""

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Calculates the maximum sum of a contiguous subarray with unique elements.
        This problem is also known as "Maximum Erasure Value".
        It uses a sliding window approach.

        :param nums: A list of integers.
        :return: The maximum sum of a subarray with unique elements.
        """
        n = len(nums)
        left = 0  # Left pointer of the sliding window.
        current_sum = 0  # Sum of the elements in the current window.
        max_sum = 0  # The maximum sum found so far.
        window_set = set()  # Stores the unique elements in the current window for fast lookups.
        
        # Iterate through the list with the right pointer to expand the window.
        for right in range(n):
            # If the current element (nums[right]) is already in our window,
            # we need to shrink the window from the left until the duplicate is removed.
            while nums[right] in window_set:
                # Remove the leftmost element from the set.
                window_set.remove(nums[left])
                # Subtract the leftmost element from the current sum.
                current_sum -= nums[left]
                # Move the left pointer to the right, shrinking the window.
                left += 1
            
            # Now that the window does not contain the duplicate of nums[right],
            # we can add the current element to the window.
            window_set.add(nums[right])
            current_sum += nums[right]
            
            # Compare the current window's sum with the global maximum sum and update if it's larger.
            # This can be done more concisely with max().
            max_sum = max(max_sum, current_sum)
            
        return max_sum