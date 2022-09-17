"""https://leetcode.com/problems/number-of-closed-islands/
1254. Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
"""
from typing import List
from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        answer = 0
        rows, columns = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(rows):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    grid[i][j] = 1
                    isClosed = True
                    while queue:
                        x, y = queue.popleft()
                        #
                        if x in (0, rows - 1) or y in (0, columns - 1):
                            isClosed = False
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if (
                                0 <= nx < rows
                                and 0 <= ny < columns
                                and grid[nx][ny] == 0
                            ):
                                queue.append((nx, ny))
                                grid[nx][ny] = 1

                    if isClosed:
                        answer += 1
        return answer
