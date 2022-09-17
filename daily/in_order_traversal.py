# Definition for a binary tree node.
"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
"""
from typing import Optional, List
<<<<<<< HEAD
=======

>>>>>>> ed69d9858fca36247597ad835589f58e28c325ad

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def inOrder(node, output):
            if not node:
                return

            if node.left:
                inOrder(node.left, output)
            output.append(node.val)
            if node.right:
                inOrder(node.right, output)
            return output

        return inOrder(root, [])
