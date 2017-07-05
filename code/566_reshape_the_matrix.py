#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-07-05 19:45 
"""


class Solution(object):
    # def matrixReshape(self, nums, r, c):
    #     flat = sum(nums, [])
    #     if len(flat) != r * c:
    #         return nums
    #     tuples = zip(*([iter(flat)] * c))
    #     return list(map(list, tuples))

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n == r * c:
            temp = []
            for row in nums:
                temp.extend(row)
            result = []
            for i in range(r):
                result.append(temp[i * c:(i + 1) * c])
            return result
        else:
            return nums


if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape([[1, 2], [3, 4]], 1, 4))
