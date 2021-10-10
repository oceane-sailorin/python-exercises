# maximum depth of binary tree

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if(root is None):
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    

s1 = Solution()

tree1 = TreeNode(1,TreeNode(9),TreeNode(20, TreeNode(15),TreeNode(7)))
print(s1.maxDepth(tree1))


tree2 = TreeNode(1,TreeNode(None),TreeNode(2))
print(s1.maxDepth(tree2))


tree3 = None
print(s1.maxDepth(tree3))


tree4 = TreeNode(0)
print(s1.maxDepth(tree4))