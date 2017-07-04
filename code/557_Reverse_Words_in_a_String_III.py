#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-07-04 20:24 
"""


class Solution(object):
    # def reverseWords(self, s):
    #     return ' '.join(s.split()[::-1])[::-1]
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        src = s.split(' ')
        dst = [x[::-1] for x in src]
        return ' '.join(dst)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
