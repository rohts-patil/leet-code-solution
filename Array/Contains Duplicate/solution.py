# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))