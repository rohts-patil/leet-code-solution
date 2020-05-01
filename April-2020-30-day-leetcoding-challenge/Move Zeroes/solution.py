### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/

class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(arr)
        for i in range(n): 
            if arr[i] != 0: 
                arr[count] = arr[i] 
                count+=1
        while count < n: 
            arr[count] = 0
            count += 1     