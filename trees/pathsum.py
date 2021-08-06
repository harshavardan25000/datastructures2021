# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        sum=0
        result=False     
        def traversal(node,sum):
            if not node:
                return 
            nonlocal result
            if not node.left and not node.right:
                if sum+node.val==targetSum:
                    result=True
            traversal(node.left,sum+node.val)
            traversal(node.right,sum+node.val)
        traversal(root,sum)
        return result
                
        