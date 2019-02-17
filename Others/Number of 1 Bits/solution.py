#  https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/565/


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c