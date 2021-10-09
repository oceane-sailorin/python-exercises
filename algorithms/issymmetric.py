# is symmetric

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right


class Solution:
        
    def isSymmetric(self, root) -> bool:
        if(root is None):
            return True
        else: 
            return self.isIndeedSymmetric(root.left, root.right)   


    def isIndeedSymmetric(self, root1, root2) -> bool:

        if(root1 is None and root2 is None):
            return True
        elif(root1 is None or root2 is None):
            return False
        elif(root1.val == root2.val):
            return self.isIndeedSymmetric(root1.left, root2.right) and self.isIndeedSymmetric(root1.right, root2.left)
        else:
            return False



s1 = Solution()

tree1 = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))



print(s1.isSymmetric(tree1))


tree2 = TreeNode(1,TreeNode(2,TreeNode(None),TreeNode(3)),TreeNode(2,TreeNode(None),TreeNode(3)))


print(s1.isSymmetric(tree2))


