"""
https://leetcode.com/problems/construct-string-from-binary-tree/
606. Construct String from Binary Tree
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def preOrderTraversal(node, output):
            if not node:
                return
            output.append(str(node.val))
            if node.left or node.right:
                output.append("(")
                preOrderTraversal(node.left, output)
                output.append(")")
            if node.right:
                output.append("(")
                preOrderTraversal(node.right, output)
                output.append(")")

            return output
