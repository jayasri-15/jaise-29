#DFS:inorder,preorder,postorder
class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def preOrderTraversal(root):
    #base Condition
    if root == None:
        return
    
    print(root.val , end=" ") #root
    preOrderTraversal(root.left)  #left
    preOrderTraversal(root.right) #right

def inOder(root):
    #base Condition
    if root == None:
        return
    inOder(root.left)  #left
    print(root.val , end=" ") #root
    inOder(root.right) #right

def postOrder(root):
    #base Condition
    if root == None:
        return    
    postOrder(root.left)  #left
    postOrder(root.right) #right
    print(root.val , end=" ") #root

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

inOder(root)




