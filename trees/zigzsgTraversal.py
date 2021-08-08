# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        level=1
        hashmap={}
        result=[]
        
        def traversal(node,level):
            if not node:
                return 
            hashmap.setdefault(level,[])
            hashmap[level].append(node.val)
            
            traversal(node.left,level+1)
            traversal(node.right,level+1)
            
        traversal(root,level)
        
        for k,v in hashmap.items():
            if k%2==0:
                result.append(v[::-1])
            else:
                result.append(v)
        return result
            
                    
                    
                    
                    
                    
                
                