class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        root = self.root
        if root==None:
            self.root = node
            return
        while(True):
            if(value<=root.data):
                if(root.left == None):
                    root.left = node
                    break
                else:
                    root = root.left
            else:
                if(root.right == None):
                    root.right = node
                    break
                else:
                    root = root.right

    # def preorder(self,root = None):
    #     if self.root == None:
    #         return
    #     if root == None:
    #         root = self.root
    #     while(root):
    #         print(root.data)
    #         if (root.left):
    #             self.preorder(root.left)
    #         if (root.right):
    #             self.preorder(root.right)
    #         break
    def inorder(self,root):
        if root == None:
            return
        while(root):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            break

# tree = BST()
# tree.insert(7)
# tree.insert(4)
# tree.insert(9)
# tree.insert(8)
# tree.insert(10)
# tree.insert(2)
# tree.preorder()
