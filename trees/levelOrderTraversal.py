class Solution:
    def levelOrder(self, root):
        hashmap,result={},[]
        level=0
        def traversal(node,level):
            nonlocal hashmap
            if not node:
                return
            hashmap.setdefault(level,[])
            hashmap[level].append(node.val)
            
            traversal(node.left,level+1)
            traversal(node.right,level+1)
            
        traversal(root,level)
        for k,v in hashmap.items():
            result.append(v)
        return result