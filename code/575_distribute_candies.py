#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-07-13 21:46 
"""


class Solution(object):
    # def distributeCandies(self, candies):
    #     return min(len(candies) / 2, len(set(candies)))
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sister = set()
        num = 0
        for candy in candies:
            if num < len(candies) / 2:
                if candy not in sister:
                    sister.add(candy)
                    num += 1
            else:
                return num
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies([1, 1, 1, 1]))
