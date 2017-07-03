#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-07-03 19:35 
"""


class Solution(object):
    # def findWords(self, words):
    #     return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1 = set('qwertyuiopQWERTYUIOP')
        l2 = set('asdfghjklASDFGHJKL')
        l3 = set('zxcvbnmZXCVBNM')
        result = []
        for word in words:
            temp = set(word)
            if temp <= l1 or temp <= l2 or temp <= l3:
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
