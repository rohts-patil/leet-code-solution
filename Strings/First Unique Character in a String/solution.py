#  https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i

        return -1 