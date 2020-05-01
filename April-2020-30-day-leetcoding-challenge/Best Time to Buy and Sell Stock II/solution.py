### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        ans = 0
        it = iter(prices)
        prev = next(it)
        for x in it:
            if x > prev:
                ans += x - prev
            prev = x
        return ans