### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/


class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (i==j):
                    continue
                else:
                    if arr[j] == arr[i]+1:
                        count = count + 1
                        break
                
        return count