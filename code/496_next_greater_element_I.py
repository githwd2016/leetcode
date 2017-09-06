#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-09-06 20:04 
"""


class Solution(object):
    # def nextGreaterElement(self, findNums, nums):
    #     """
    #     :type findNums: List[int]
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     d = {}
    #     st = []
    #     ans = []
    #
    #     for x in nums:
    #         while len(st) and st[-1] < x:
    #             d[st.pop()] = x
    #         st.append(x)
    #
    #     for x in findNums:
    #         ans.append(d.get(x, -1))
    #
    #     return ans
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in findNums:
            index = nums.index(i)
            value = -1
            for j in nums[index + 1:]:
                if j > i:
                    value = j
                    break
            result.append(value)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
