# issametree
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:
        if(p is None and q is None):
            return True
        elif(p is None or q is None):
            return False

        if(p.val==q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    

s1 = Solution()

tree11 = TreeNode(1,TreeNode(2),TreeNode(3))
tree21 = TreeNode(1,TreeNode(2),TreeNode(3))

print(s1.isSameTree(tree11,tree21))


tree12 = TreeNode(1,TreeNode(2))
tree22 = TreeNode(1,TreeNode(None),TreeNode(2))

print(s1.isSameTree(tree12,tree22))


tree13 = TreeNode(1,TreeNode(2),TreeNode(1))
tree23 = TreeNode(1,TreeNode(1),TreeNode(2))

print(s1.isSameTree(tree13,tree23))