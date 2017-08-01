#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-08-01 21:47 
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[-1::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString("hello"))
