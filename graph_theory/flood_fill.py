"""733. Flood Fill
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color."""

from typing import List

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        old_color = image[sr][sc]
        if not image:
            return []
        if image[sr][sc] == color:
            return image

        def dfs(i, j):
            if (
                i < 0
                or i >= len(image)
                or j < 0
                or j >= len(image[0])
                or image[i][j] != old_color
            ):
                return
            image[i][j] = color
            for x, y in directions:
                dfs(i + x, j + y)

        dfs(sr, sc)
        return image
