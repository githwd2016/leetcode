#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-09-05 20:56 
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def trimBST(self, root, L, R):
    #     def trim(node):
    #         if node:
    #             if node.val > R:
    #                 return trim(node.left)
    #             elif node.val < L:
    #                 return trim(node.right)
    #             else:
    #                 node.left = trim(node.left)
    #                 node.right = trim(node.right)
    #                 return node
    #
    #     return trim(root)
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root:
            if L <= root.val <= R:
                root.left = self.trimBST(root.left, L, R)
                root.right = self.trimBST(root.right, L, R)
                return root
            elif root.val < L:
                return self.trimBST(root.right, L, R)
            else:
                return self.trimBST(root.left, L, R)
        else:
            return None
