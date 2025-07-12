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

def insertNode(root,newVal):
    if root.left==None and newVal<root.val:
        root.left=TreeNode(newVal)
        return
    if root.right==None and newVal>root.val:
        root.right=TreeNode(newVal)
        return
    if newVal<root.val:
        insertNode(root.left,newVal)
    if newVal>root.val:
        insertNode(root.right,newVal)

