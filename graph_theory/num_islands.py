""" https://leetcode.com/problems/number-of-islands/ 
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water"""
from typing import List
from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    queue = deque([(row, col)])
                    while queue:
                        current_row, current_column = queue.popleft()
                        for x, y in directions:
                            if (
                                0 <= current_row + x < len(grid)
                                and 0 <= current_column + y < len(grid[0])
                                and grid[current_row + x][current_column + y] == "1"
                            ):
                                queue.append((current_row + x, current_column + y))
                                grid[current_row + x][current_column + y] = "0"
                    count += 1
        return count
