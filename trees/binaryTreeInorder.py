class Node:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
root=Node(1)
root.right=Node(2)
root.right.left=Node(3)

def binaryTreeInorder(root):

    result=[]

    def traversal(node):
        if not node:
            return
        traversal(node.left)
        result.append(node.val)
        traversal(node.right)
    traversal(root)
    print(result)
binaryTreeInorder(root)

