class Solution:
    def maxPathSum(self, root) -> int:
        global_sum=float('-inf')
        
        def traversal(node):
            nonlocal global_sum
            if not node:
                return 0
            left_sum=traversal(node.left)
            right_sum=traversal(node.right)

            local_sum=node.val+left_sum+right_sum
            global_sum=max(global_sum,local_sum,node.val,node.val+right_sum,node.val+left_sum)
            
            return max(node.val,node.val+left_sum,node.val+right_sum)
        
        traversal(root)
        return global_sum