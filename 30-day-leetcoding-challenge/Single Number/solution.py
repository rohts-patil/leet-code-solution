### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in range(1,len(nums)): 
            a = a ^ nums[i]
        return a