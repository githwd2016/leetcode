#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-06-22 21:56 
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def mergeTrees(self, t1, t2):
    #     if not t1 and not t2: return None
    #     ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    #     ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
    #     ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    #     return ans
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        res = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        res.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        res.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return res


if __name__ == '__main__':
    pass
