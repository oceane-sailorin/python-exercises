# binary tree target sum
"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if(root is None):
            return False
        remains = 0
        
        if( root.val == targetSum and root.left == None and root.right == None):
            return True
        else:
            if root.val is not None:
                remains = targetSum - root.val
            return self.hasPathSum(root.left ,remains ) or self.hasPathSum(root.right ,remains)    
    
            
       
    
  #examples  

s1 = Solution()

tree1 = TreeNode(5,TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)),TreeNode(None)),TreeNode(8, TreeNode(13),TreeNode(4, TreeNode(None), TreeNode(1))))
print(s1.hasPathSum(tree1,22))

tree2 = TreeNode(1,TreeNode(2),TreeNode(3))
print(s1.hasPathSum(tree2,5))

tree3 = None
print(s1.hasPathSum(tree3,5))

tree4 = TreeNode(0)
print(s1.hasPathSum(tree4,0))

tree5 = TreeNode(5,TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)),TreeNode(None)),TreeNode(8, TreeNode(13),TreeNode(4, TreeNode(None), TreeNode(1))))
print(s1.hasPathSum(tree5,25))

tree6 = TreeNode(1,TreeNode(2),TreeNode(3))
print(s1.hasPathSum(tree6,3))

tree7 = TreeNode(5,TreeNode(6, TreeNode(15, TreeNode(7), TreeNode(2)),TreeNode(None)),TreeNode(8, TreeNode(8),TreeNode(4, TreeNode(4), TreeNode(1))))
print(s1.hasPathSum(tree7,21))