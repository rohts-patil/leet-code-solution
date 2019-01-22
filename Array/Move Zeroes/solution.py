# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)