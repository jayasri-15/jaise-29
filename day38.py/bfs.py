#BFS
from collections import deque
class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root):
    queue=deque([root])
    while queue:
        current=queue.popleft()
        print(current.val,end=" ")
        if current.left!=None :queue.append(current.left)
        if current.right!=None :queue.append(current.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(9)
root.left.left.right = TreeNode(10)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(11)

root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(8) 

levelOrder(root)




