#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-06-30 20:40 
"""


class Solution(object):
    # def findComplement(self, num):
    #     i = 1
    #     while i <= num:
    #         i = i << 1
    #     return (i - 1) ^ num
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i <<= 1
        return i - 1 - num

if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(1))
