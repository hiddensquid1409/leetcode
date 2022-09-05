"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 """
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        """Return the level order traversal of the tree.
        Based on the BFS algorithm.

        Args:
            root (Node): The root node of the tree.

        Returns:
            List[List[int]]: The level order traversal of the tree.
        """
        result = []
        queue = deque([root] if root else [])
        while queue:
            result.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                result[-1].append(node.val)
                queue.extend(node.children)

        return result
