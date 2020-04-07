### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n; 
        fast = n; 
        while(True): 
            slow = self.numSquareSum(slow); 
            fast = self.numSquareSum(self.numSquareSum(fast)); 
            if(slow != fast): 
                continue; 
            else: 
                break; 
        return (slow == 1); 
        
        
    def numSquareSum(self,n): 
        squareSum = 0; 
        while(n): 
            squareSum += (n % 10) * (n % 10); 
            n = int(n / 10); 
        return squareSum;
        