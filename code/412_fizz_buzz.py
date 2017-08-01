#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-08-01 21:54 
"""


class Solution(object):
    # def fizzBuzz(self, n):
    #     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
