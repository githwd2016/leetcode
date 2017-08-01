#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: winton 
@time: 2017-08-01 22:10 
"""


class Solution(object):
    # def islandPerimeter(self, grid):
    #     return sum(sum(map(operator.ne, [0] + row, row + [0]))
    #                for row in grid + map(list, zip(*grid)))
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        for i in grid:
            i.insert(0, 0)
            i.append(0)
        grid.insert(0, [0] * (n + 2))
        grid.append([0] * (n + 2))
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i][j]:
                    if not grid[i - 1][j]:
                        perimeter += 1
                    if not grid[i + 1][j]:
                        perimeter += 1
                    if not grid[i][j - 1]:
                        perimeter += 1
                    if not grid[i][j + 1]:
                        perimeter += 1
        return perimeter

if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
