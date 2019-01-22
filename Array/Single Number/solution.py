# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
        