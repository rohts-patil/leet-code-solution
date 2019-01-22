# https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        
        # build up the dict of number
        # counts from the first list
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        # check if the numbers in the
        # second list occur in the dict
        for num in nums2:
            if num in d:
                if d[num] > 0:
                    d[num] -= 1
                    result.append(num)
                    
        return result