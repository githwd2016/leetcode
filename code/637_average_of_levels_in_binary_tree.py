#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-09-07 21:08 
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def averageOfLevels(self, root):
    #     info = []
    #
    #     def dfs(node, depth=0):
    #         if node:
    #             if len(info) <= depth:
    #                 info.append([0, 0])
    #             info[depth][0] += node.val
    #             info[depth][1] += 1
    #             dfs(node.left, depth + 1)
    #             dfs(node.right, depth + 1)
    #
    #     dfs(root)
    #
    #     return [s / float(c) for s, c in info]
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        result = []
        while queue:
            result.append(sum([x.val for x in queue]) / len(queue))
            temp = []
            for e in queue:
                if e.left:
                    temp.append(e.left)
                if e.right:
                    temp.append(e.right)
            queue = temp
        return result
