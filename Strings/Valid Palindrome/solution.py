#  https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS= [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]