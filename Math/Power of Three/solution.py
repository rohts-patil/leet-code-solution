#  https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/745/
#  1162261467 is 3^19,  3^20 is bigger than int


class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        return n > 0 and 1162261467 % n == 0