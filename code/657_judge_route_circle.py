#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-09-04 19:54 
"""


class Solution(object):
    # def judgeCircle(self, moves):
    #     return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return True if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D') else False

if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle('LL'))
