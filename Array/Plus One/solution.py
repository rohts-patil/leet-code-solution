# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        prev = 1
        for i in range(len(digits)):
            digits[i] += prev
            if digits[i] == 10:
                digits[i] = 0
                prev = 1
            else:
                prev = 0
        if prev == 1:
            digits.append(1)
        return digits[::-1]