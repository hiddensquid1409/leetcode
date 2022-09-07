"""
https://leetcode.com/problems/binary-tree-pruning/

814. Binary Tree Pruning

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        output = []

        def order_traversal(node):
            if not node:
                return
            if node.val == 1:
                output.append(node)
            order_traversal(node.left)
            order_traversal(node.right)
            
        def reconstruct_tree(nodes):
            if not nodes:
                return None
            node = nodes.pop(0)
            node.left = reconstruct_tree(nodes)
            node.right = reconstruct_tree(nodes)
            return node

        order_traversal(root)
        output_tree= reconstruct_tree(output)
        
        return output_tree
   



if __name__ == "__main__":
    input_tree = TreeNode(
        1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1))
    )
    print(Solution().pruneTree(input_tree))
