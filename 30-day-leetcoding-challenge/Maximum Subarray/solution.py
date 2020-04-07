### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

class Solution(object):
    def maxSubArray(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        size  = len(a)
        max_so_far =a[0] 
        curr_max = a[0] 
        for i in range(1,size): 
            curr_max = max(a[i], curr_max + a[i]) 
            max_so_far = max(max_so_far,curr_max) 
        return max_so_far