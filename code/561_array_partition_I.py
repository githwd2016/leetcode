#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-06-29 20:23 
"""


class Solution(object):
    # def arrayPairSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     return sum(sorted(nums)[::2])
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums[::2])
