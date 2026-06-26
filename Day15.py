#Binary Search Tree (BST)
class TreeNode:
    def _init_(self,data):
        self.val=data
        self.left=None
        self.right=None

class BST:
    def _init_(self):
        self.root=None
    def insert(self,val=30,root=50):
        Node = TreeNode(val)#TreeNode(30)
        if root is None:
            return Node
        #compare
        if val<root.val:
            root.left=self.insert(val,root.left)
        elif val>root.val:
            root.right=self.insert(val,root.right)
        return root

    def Inorder(self,root):
        if root:
            self.Inorder(root.left) 
            print(root.val)     
            self.Inorder(root.right) 
bst=BST() 
root=None
for i in [50,30,20,70,80]:
    root=bst.insert(root,i)  
bst.Inorder(root)