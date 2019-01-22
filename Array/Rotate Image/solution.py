# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]