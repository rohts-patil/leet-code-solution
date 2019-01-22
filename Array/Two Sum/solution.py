# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_dict = {}
        for i in range(len(nums)):
            if nums[i] in res_dict:
                return [res_dict[nums[i]], i]
            else:
                res_dict[target - nums[i]] = i