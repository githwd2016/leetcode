#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-06-27 21:34 
"""


class Solution(object):
    # def hammingDistance(self, x, y):
    #     """
    #     :type x: int
    #     :type y: int
    #     :rtype: int
    #     """
    #     return bin(x^y).count('1')
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        while x > 0 and y > 0:
            x_remainder = x % 2
            y_remainder = y % 2
            x //= 2
            y //= 2
            if x_remainder != y_remainder:
                result += 1
        z = max(x, y)
        while z > 0:
            remainder = z % 2
            z //= 2
            if remainder == 1:
                result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
