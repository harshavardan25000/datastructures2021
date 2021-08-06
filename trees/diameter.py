class Node:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
root=Node(2)
root.left=Node(4)
root.right=Node(5)
root.left.left=Node(5)
root.left.right=Node(6)

def diameterBT(root):
    diameter=0

    def longestPath(node):
        if not node:
            return 0
        nonlocal diameter
        leftpath=longestPath(node.left)
        rightpath=longestPath(node.right)
        diameter=max(diameter,leftpath+rightpath)

        return 1+max(leftpath,rightpath)

    longestPath(root)
    print(diameter)
diameterBT(root)


